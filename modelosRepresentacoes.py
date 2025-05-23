from nltk.corpus import gutenberg
from nltk import tokenize
import nltk
import math
import numpy as np

#1 PASSO: CARREGAR O CORPUS
texto = gutenberg.raw('austen-emma.txt')
frase = texto[50:477]
#print(frase)
frase = frase.lower().split("\n")
treino =texto.lower().split("\n") 
#print(frase)

#2 PASSO: TOKENIZAR O CORPUS
textoToken = []
for linha in frase:
    token = tokenize.word_tokenize(linha, language='english')
    textoToken.append(token)
#print(textoToken)    
treinoToken = []
for linha in treino:
    token = tokenize.word_tokenize(linha, language="english")
    treinoToken.append(token)

#3 PASSO: ADICIONAR OS PADS DE INICIO E FIM EM CADA DOCUMENTO/LINHA
from nltk.lm.preprocessing import pad_both_ends

n = 2
textoTokenPad = []
for linha in textoToken:
    padded = list(pad_both_ends(linha, n=n))
    textoTokenPad.append(padded)
#print(textoTokenPad)  

#4 PASSO: CALCULANDO OS N-GRAMAS(NESSE CASO BIGRAMA)
ngramas = 2
bigramas = []
for linha in textoTokenPad:
    bigrama = list(nltk.ngrams(linha, n=ngramas))
    bigramas.append(bigrama)
#print(bigramas)    

#Para fazer o modelo é necessário realizar os n-gramas menores
from nltk.util import everygrams
tam_ngramas = 3
ngramasTexto = []
for linha in textoTokenPad:
    ngramas = list(everygrams(linha, max_len=tam_ngramas))
    ngramasTexto.append(ngramas)
#print(ngramasTexto)

#5 PASSO: COLOCAR OS TOKENS COM PADS EM UMA ÚNICA LISTA
from nltk.lm.preprocessing import flatten

token = list(flatten(textoTokenPad))
#print(token)

#6 PASSO: DEFINIR O VOCABULÁRIO
from nltk.lm import Vocabulary

vocab = Vocabulary(token, unk_cutoff=1)
#print(vocab.counts)

#COMANDO QUE FAZ OS 3-6 PASSOS
from nltk.lm.preprocessing import padded_everygram_pipeline

ngramas = 3
ngramasPad, vocab = padded_everygram_pipeline(ngramas, treinoToken)


#PASSO 7: TREINANDO UM MODELO DE LINGUAGEM
from nltk.lm import MLE, Laplace, Lidstone

modelo = Lidstone(1, ngramas)#Ele acrescenta 1 ao dividendo para evitar casos de probabilidade 0
modelo.fit(ngramasPad, vocab)
palavras = modelo.generate(5, text_seed=[","])
#print(palavras)
#print(modelo.score("in", [","]))
#O modelo.score calcula a probabilidade de in aprecer depois de uma , pegando o numero de caso que tem ",in" dividindo pelo número de , que tem no corpus
def perplexidade(modelo, sentenca_tokenizada, n):
    ngrams = list(everygrams(pad_both_ends(sentenca_tokenizada, n), max_len=n))
    N = len(ngrams)
    soma_log = 0
    for ng in ngrams:
        contexto = list(ng[:-1])
        palavra = ng[-1]
        prob = modelo.score(palavra, contexto)
        if prob > 0:
            soma_log += math.log(prob)
        else:
            return float("inf")  
    return math.exp(-soma_log / N)

#print(perplexidade(modelo, textoToken, ngramas))#Quanto maior a perplexidade, maior a confusão do modelo
#print(modelo.score("emma", context=["woodhouse"]))

#Representações
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown="ignore")
X = [["o"], ["menino"], ["foi"], ["para"], ["a"], ["escola"], ["de"], ["ônibus"]]

enc.fit(X)

vocab = enc.categories_[0]
#print(vocab)
vetores = enc.transform(X).toarray()#As linhas representam a frase e as colunas como o vocabulário está distribuído
#print(vetores)

from sklearn.feature_extraction.text import CountVectorizer

poema = ["A festa acabou e apagou quando a luz apagou e acabou,", "A luz acabou", "E agora, José?", "A festa acabou,", "a luz apagou,", "o povo sumiu,", "a que zomba os outros,", "você que faz versos,", "que ama, protesta?", "e agora, José?"]

def tokenize(text):
    return nltk.word_tokenize(text, language="portuguese")

vectorizer = CountVectorizer(tokenizer=tokenize, lowercase = True)

vetores = vectorizer.fit_transform(poema)#Cada linha representa um documento e cada coluna a frequência de cada palavra do vocabulário no documento
vocab = vectorizer.get_feature_names_out()
#print(vetores.toarray())
#print(vocab)

corpus_token = []
for verso in poema:
    tokenizado = str(tokenize(verso.lower()))
    corpus_token.append(tokenizado)

matriz = np.zeros((len(vocab), len(vocab)))    

for verso in corpus_token:#Vai gerar uma matriz de correlações, onde cada célula representa o número de vezes que as duas palavras se encontram juntas
    for i, w1 in enumerate(vocab):
        for j, w2 in enumerate(vocab):
            if i != j:
                if w1 in verso and w2 in verso: 
                    matriz[i, j] += 1

#print(matriz)                    

#TF-IDF
#tf(t,d) = número de vezes que o termo t aparece no documento d/ número de termos no d
#idf(t) = N(número de documentos)/1 + log(DF(t)(Número de documentos em que o termo t aparece))
#As linhas representam os documentos e as colunas o vocabulário, cada célula representa o peso delas no documento

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

vectorizer = Pipeline([("count", CountVectorizer()), ("tfdf", TfidfTransformer())])#O vectorizer percorre um caminho, primeira fazendo a transformação do texto bruto em uma matriz de contagem e depois gera uma matriz tfdf com o resultados

vetores = vectorizer.fit_transform(poema)
vocab = vectorizer["count"].get_feature_names_out()
#print(vocab)
#print(vetores.toarray())