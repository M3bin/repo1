from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
iris=load_iris();

features=iris.data
labels=iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(features,labels,test_size=.3)

knn=KNeighborsClassifier()
knn.fit(X_train,Y_train)

p=knn.predict(X_test)

from sklearn.metrics import accuracy_score
print ("accuracy=",accuracy_score(Y_test,p))





