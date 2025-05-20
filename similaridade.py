import pandas as pd
import numpy as np

texts = ["Goku is a hero in the Dragon Ball since 1989! Goku saved the earth so many times.",
         "The 7 Dragon Balls can make wishes come true! Each ball contains his own dragon.",
         "If the wishes are superfluos, the dragon balls will become dark.", 
         "Seiya is a bronze knight and is one of the main Knights of the zodiac. He saved Athena several times.",
         "A knight of the zodiac wear a bronze, silver or a gold cloth to protect Athena.",
         "Saint Seiya: Knights of the Zodiac is a japanese manga in which mystical warriors called the Saints fight wearing sacred cloths."]

df = pd.DataFrame({
    'texts' : texts,
})

#print(df)

#Similaridade baseada na distância de caracteres(Levenshtein)

def levenshtein(seq1, seq2):
    sizeX = len(seq1) + 1
    sizeY = len(seq2) + 1
    matriz = np.zeros((sizeX, sizeY))
    for x in range(sizeX):
        matriz[x,0] = x
    for y in range(sizeY):
        matriz[0,y] = y  
    for x in range(1, sizeX):
        for y in range(1, sizeY):
            if seq1[x-1] == seq2[y-1]:
                matriz[x, y] = matriz[x-1, y-1]
            else:
                matriz[x, y] = min(
                    matriz[x-1, y] + 1,
                    matriz[x, y-1] + 1,
                    matriz[x-1, y-1] + 1
                )        
    print(pd.DataFrame(matriz[1:, 1:], index=list(seq1), columns=list(seq2)))
    
    return matriz[sizeX-1, sizeY-1]

#print(levenshtein("cacetada", "carambola"))

#levenshtein(df.loc[2]['texts'], df.loc[5]['texts'])

#Similaridade baseada em termos

from sklearn.feature_extraction.text import CountVectorizer

vetorizador = CountVectorizer(
    lowercase=True,
    stop_words="english",
    min_df=2,
    dtype=np.int16
)

vetorizador.fit(df['texts'])
#print(vetorizador.get_feature_names_out())

represent = vetorizador.transform(df["texts"])
rep_array = represent.toarray()
#print(rep_array)

from sklearn.metrics.pairwise import cosine_similarity

matrizSim = cosine_similarity(rep_array)
#print(matrizSim)

def bestSim(id, matriz):
    matrizSimility = cosine_similarity(matriz)
    bestId = -1
    bestSimilty = -1
    for id_for, doc_sim in enumerate(matrizSimility[id]):
        if id_for != id:
            if doc_sim > bestSimilty:
                bestId = id_for
                bestSimilty = doc_sim           
    return bestId

print(f"O texto mais parecido com o 5 é {df.loc[bestSim(5, rep_array)]["texts"]}")            