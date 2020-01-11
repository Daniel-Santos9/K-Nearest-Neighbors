from sklearn.neighbors import KNeighborsClassifier 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Carregando os dados do dataset.
base = load_iris()

#fazendoa separação de treinamento e teste
previsores_train, previsores_test, classe_train, classe_test = train_test_split(base.data, base.target, test_size=0.3)

#Fazendo a classificação
classificador = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classificador.fit(previsores_train,classe_train)

predict = classificador.predict(previsores_test)

acc_dataTrain = classificador.score(previsores_train, classe_train)

acc_dataTest = classificador.score(previsores_test,classe_test) 

acc = accuracy_score(classe_test, predict)

print(acc_dataTrain)
print(acc_dataTest)
print(acc)