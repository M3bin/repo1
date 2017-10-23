from sklearn.tree import DecisionTreeClassifier

features=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,30],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]
labels=[1,1,0,0,1,1,0,0,0,1,1]

clf=DecisionTreeClassifier()
clf.fit(features,labels)

print ("enter height: ")
h=int(input())
print ("enter weight: ")
w=int(input())
print("enter shoe size: ")
s=int(input())
l=[[h,w,s]]
p=clf.predict(l)
if p==1:
	print("male")
elif p==0:
	print("female")
else:
	print("error")

