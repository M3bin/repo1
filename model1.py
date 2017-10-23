from sklearn.tree import DecisionTreeClassifier

features=[[140,0],[130,0],[150,1],[170,1]]
labels=[0,0,1,1]

clf=DecisionTreeClassifier()
clf.fit(features,labels)

print ("enter weight: ")
w=int(input())
print ("enter dimension: ")
d=int(input())
l=[[w,d]]
p=clf.predict(l)
if p==1:
	print("orange")
elif p==0:
	print("apple")
else:
	print("error")

