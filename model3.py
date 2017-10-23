from sklearn.datasets import load_iris
import numpy as np	#for math operations as data set is matrix
from sklearn.tree import DecisionTreeClassifier

iris=load_iris()	#laod all values into variable iris
#print(iris.feature_names)
#print(iris.target_names)
#print(iris.data[0])
#print(iris.target[0])

x=[0,50,100]
xtrain=np.delete(iris.data,x,axis=0)	#if no axis given,reshape error occurs
ytrain=np.delete(iris.target,s)

xtest=iris.data[x]
ytest=iris.target.[x]

clf=DecisionTreeClassifier()
cls.split(xtrain,ytrain)

print(ytest)
print("prediction=",clf.predict(xtest))

