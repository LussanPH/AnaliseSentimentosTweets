from nltk.corpus import gutenberg
from nltk import tokenize
import nltk

#1 PASSO: CARREGAR O CORPUS
texto = gutenberg.raw('austen-emma.txt')
frase = texto[50:477]
#print(frase)
frase = frase.lower().split("\n")
#print(frase)

#2 PASSO: TOKENIZAR O CORPUS
textoToken = []
for linha in frase:
    token = tokenize.word_tokenize(linha, language='english')
    textoToken.append(token)
#print(textoToken)    

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
ngramasPad, vocab = padded_everygram_pipeline(ngramas, textoToken)

#PASSO 7: TREINANDO UM MODELO DE LINGUAGEM
from nltk.lm import MLE

modelo = MLE(ngramas)
modelo.fit(ngramasPad, vocab)
palavras = modelo.generate(5, text_seed=[","])
#print(palavras)
#print(modelo.score("in", [","]))
#O modelo.score calcula a probabilidade de in aprecer depois de uma , pegando o numero de caso que tem ",in" dividindo pelo número de , que tem no corpus
#Estudar Perplexidade e Suavização