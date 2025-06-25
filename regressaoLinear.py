import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
temperatura = np.array([30, 25, 36, 18, 25, 29, 30, 33, 37, 31, 26, 37, 29, 26, 30, 31, 34, 38])
numero_sorvetes = np.array([20, 12, 50, 10, 18, 25, 26, 32, 48, 22, 16, 52, 24, 20, 28, 29, 35, 40])
df = pd.DataFrame({'temperatura': temperatura, 'numero_sorvetes': numero_sorvetes})
#plt.plot(df['temperatura'], df['numero_sorvetes'], '*')
#plt.xlabel('Temperatura')
#plt.ylabel('Sorvetes')
#plt.show()

x = df['temperatura'].to_numpy()#Tranforma em float a variável independente
y = df['numero_sorvetes'].to_numpy()#Variável dependente

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2)

from sklearn.linear_model import LinearRegression
modelo = LinearRegression()
modelo.fit(x_treino.reshape(-1, 1), y_treino.reshape(-1, 1))#O reshape tranforma o x e o y em um vetor de n linha e 1 coluna

y_previsto = modelo.predict(x_teste.reshape(-1, 1))

plt.plot(range(y_previsto.shape[0]), y_previsto, 'r--')
plt.plot(range(y_teste.shape[0]), y_teste, 'g--')
plt.legend(['Sorvetes previstos','Sorvetes vendidos'])
plt.xlabel('Índice')
plt.ylabel('Sorvetes')
plt.show()

