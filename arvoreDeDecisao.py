#Possui vários índices que determinam como a árvore vai ser decidida, o padrão é o Gini
'''
Gini = 1 - somatório de cada um dos lados de uma árvore ao quadrado
'''
#Exemplo: classificação entre salmão e Seabass, divisão de brilo >0.7
'''
>0.7: 1 Seabass e 0 salmão
<=0.7: 3 Seabass e 5 salmão
'''
#Lado dos maiores que 0.7:
'''
G = 1 - [(1/1)² + (0/1)²] = 0
Calcula a impureza dos dados, nesse lado foi perfeita a divisão
'''
#Lado dos menores ou iguais a 0.7:
'''
G = 1 - [(3/8)² + (5/8)²] = 0.47
Nesse lado a impureza foi grande
'''
#Impureza Total:
'''
G = 1 - [(1/9 * 1) + (8/9) * 0.53] = 0.42
Quanto menor o Gini total, melhor a divisão será. Logo a divisão em brilho >0.7 não é boa
'''

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

dtc = DecisionTreeClassifier(max_depth=6)#A profundidade evita o overfitting, fazendo com que ele consiga generalizar os padrões
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
dtc.fit(X_train, y_train)
print(dtc.score(X_test, y_test))

dtr = DecisionTreeRegressor(max_depth=8)
X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
dtr.fit(X_train, y_train)
print(dtr.score(X_test, y_test))

from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
dtc.fit(X, y)
print(dtc.feature_importances_)#As colunas com 0 represenatam features irrelevantes e quanto mais próximo de 1 maior sua importância, Elas se correlacionam, a retirada de uma implica em outra
