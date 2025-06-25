#Queremos saber a distância euclidiana entre 2 e 5, pegamos a diferença, elevamos ao quadrado, e tiramos a raiz
print(((2-5)**2)**0.5)

a = [2.0, 0.75]
b = [5.0, 0.50]

print(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5)#Distância euclidiana dos pontos

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)#Define que no treinamento cada dado acrescentado vai ver os três dados vizinhos e classificar o dado com rotulo que possui mais vizinhos

import pandas as pd
data = pd.read_table("fruit_data_with_colors.txt")

X = data[['mass', 'height', 'width', 'color_score']]
y = data['fruit_label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

knn.fit(X_train, y_train)

print(knn.score(X_test, y_test))

from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()#Ele transforma os dados em valores entre 0 e 1, diminuindo a distância entre as grandezas

X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))

from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import fetch_california_housing
knn = KNeighborsRegressor()
data = fetch_california_housing()
X, y = fetch_california_housing(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y)

#X_train = mm.fit_transform(X_train)
#X_test = mm.transform(X_test)

knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
