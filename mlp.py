from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import MinMaxScaler

X,y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
mm = MinMaxScaler()
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
mlp = MLPRegressor(hidden_layer_sizes=(100, 100, 50), max_iter=1000)#hidden layers são as camadas intermediárias com a qiuantidade de neurônios espeificadas, e o max_iter se refere a quantidade de épocas
mlp.fit(X_train, y_train)
print(mlp.score(X_test, y_test))