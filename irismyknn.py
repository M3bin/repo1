from scipy.spatial import distance			#use euclidian distance finding formula

def eucli(a,b):
	return distance.euclidean(a,b)

class myknn():
	def fit(self,X_train,Y_train):			#fit method
		self.X_train=X_train
		self.Y_train=Y_train
	def predict(self,X_test):			#predict method fir test data
		predictions =[]
		for row in  X_test:
			label=self.closest(row)
			predictions.append(label)
		return predictions
	def closest(self,row):
		best_dist=eucli(row,self.X_train[0])
		best_index=0
		for i in range(1,len(self.X_train)):
			dist=eucli(row,self.X_train[i])
			if dist<best_dist:
				best_dist=dist
				best_index=i
		return self.Y_train[best_index]

#from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
iris=load_iris()

features=iris.data
labels=iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(features,labels,test_size=.3)

knn=myknn()
knn.fit(X_train,Y_train)

p=knn.predict(X_test)

from sklearn.metrics import accuracy_score
print ("accuracy=",accuracy_score(Y_test,p))





