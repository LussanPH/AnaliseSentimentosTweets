import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("car_data.csv")
print(df.shape)

#print(df['tipo_combustivel'].unique())
#print(df['tipo_vendedor'].unique())
#print(df['tipo_transmissao'].unique())
df['tipo_combustivel'].replace({'Gasolina':0, 'Diesel':1, 'GasNatural':2}, inplace=True)
df['tipo_vendedor'].replace({'Revendedor':0, 'Individual':1}, inplace=True)
df['tipo_transmissao'].replace({'Manual':0, 'Automatico':1}, inplace=True)

plt.scatter(df['ano'], df['preco_venda'], color='blue')
plt.xlabel("Anos")
plt.ylabel("Preço de venda")
plt.show()

plt.scatter(df['ano'], df['kms_rodados'],  color='red')
plt.xlabel("Ano do Carro")
plt.ylabel("Kms Rodados")
plt.show()

# escolhendo as variáveis independentes
x = df[['ano', 'preco_atual', 'kms_rodados', 'tipo_combustivel', 'tipo_vendedor', 'tipo_transmissao', 'n_donos']]

# variável dependente
y = df[['preco_venda']]

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2)

from sklearn.linear_model import LinearRegression

modelo = LinearRegression()

modelo.fit(x_treino, y_treino)

y_previsao = modelo.predict(x_teste)

plt.plot(range(y_previsao.shape[0]), y_previsao, 'r--')
plt.plot(range(y_previsao.shape[0]), y_teste, 'g--')
plt.legend(['Preço previsto', 'Preço verdadeiro'])
plt.xlabel('Índice')
plt.ylabel('Preço')
plt.show()

from sklearn.metrics import r2_score

print('R2-score: ', r2_score(y_teste, y_previsao))