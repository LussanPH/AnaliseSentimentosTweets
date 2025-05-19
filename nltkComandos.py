import nltk
import numpy
#nltk.download("gutenberg") Corpus 
#nltk.download("punkt") Tokenizadores
#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.corpus import gutenberg

#print(gutenberg.fileids()[:3])
words = gutenberg.words('austen-emma.txt')
texto = gutenberg.raw('austen-emma.txt')
fraseInicio = texto[50:139]
#print(words)
#print(fraseInicio)

#print(stopwords.words("portuguese"))

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

sentTokenize = nltk.sent_tokenize(fraseInicio)
#print(sentTokenize)
wordTokenize = nltk.word_tokenize(fraseInicio)
#print(wordTokenize)

from nltk.tokenize import TweetTokenizer
texto2 = "I'm very veryyy hapyyyyyy #betterlife @barneys :D :)"
wordTweet = word_tokenize(texto2)
tweet = TweetTokenizer()
tweetToken = tweet.tokenize(texto2)
#print(wordTweet)
#print(tweetToken)
tweet2 = TweetTokenizer(reduce_len=True, strip_handles=True)
tweetToken2 = tweet2.tokenize(texto2)
#print(tweetToken2)

from nltk.stem.snowball import SnowballStemmer
snowBallStemmer = SnowballStemmer("portuguese")
radical = snowBallStemmer.stem("computação")
#print(radical)

from nltk.stem.wordnet import WordNetLemmatizer
#nltk.download("wordnet")
wordNetLemmatizer = WordNetLemmatizer()
lema = wordNetLemmatizer.lemmatize("rocks")
lema2 = wordNetLemmatizer.lemmatize("corpora")
#print(lema)
#print(lema2)
lema3 = wordNetLemmatizer.lemmatize("better", pos="a")
lema4 = wordNetLemmatizer.lemmatize("clustering", pos="v")
#print(lema3)
#print(lema4)

#nltk.download("averaged_perceptron_tagger")#vai ver a classificação de substantivo, adjetivo, etc
#nltk.download("averaged_perceptron_tagger_eng")#Especifico para palavras em inglês
#nltk.download("maxent_ne_chunker")#reconhece entidades nomeadas
#nltk.download("maxent_ne_chunker_tab")#Suporte para o maxent_ne-chunker
#nltk.download("words")#conjunto de palavras em inglês

text3 = "Ishowspeed will make a tour in Google"
print(nltk.ne_chunk(nltk.pos_tag(word_tokenize(text3))))