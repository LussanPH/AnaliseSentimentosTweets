import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("Mall_Customers.csv")
print(df.isnull().sum())#Verifica se tem algum elemento nulo nas coluna
print(df.head())

plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], marker='.')
plt.xlabel("Renda Anual")
plt.ylabel("Score(1-100)")
plt.show()

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

modelo = KMeans(n_clusters=5, init='k-means++')
y_kmeans = modelo.fit_predict(X)

k_grupos = 5
cores = ['r', 'g', 'b', 'k', 'y']

for i in range(k_grupos):
    cluster = X[y_kmeans == i]
    plt.scatter(cluster['Annual Income (k$)'], cluster['Spending Score (1-100)'], s = 50, c= cores[i], label= f'cluster {i}')

plt.title("Gruposde clientes")
plt.xlabel("Renda dos clientes")
plt.ylabel("Score dos clientes")
plt.legend()
plt.show()    

X = df[['Age', 'Spending Score (1-100)']]
modelo = KMeans(n_clusters=5, init="k-means++")
y_previsao = modelo.fit_predict(X)

k_grupos = 5
cores = ['r', 'g', 'b', 'y', 'k']

for i in range(k_grupos):
    cluster = X[y_previsao==i]
    plt.scatter(cluster['Age'], cluster['Spending Score (1-100)'], s=75, c=cores[i], label=f'Cluster {i}')

plt.title("Grupo de clientes")
plt.xlabel("Idade")
plt.ylabel("Score")
plt.legend()
plt.show()   
