n=0
ls=[]
print ("enter list limit")
cnt=int(input())
for i in range(0,cnt):
	tmp=int(input())
	ls.append(tmp)
while(1):
	opr=input()
	opr1=opr.split(" ")
	if(opr1[0]=="append"):
		ls.append(int(opr1[1]))
		print(ls)
	elif(opr1[0]=="reverse"):
		ls.reverse()
		print(ls)
	elif(opr1[0]=="sort"):
		ls.sort()
		print(ls)
	elif(opr1[0]=="pop"):
		ls.pop()
		print(ls)
	elif(opr1[0]=="print"):
		print(ls)
	elif(opr1[0]=="count"):
		numcnt=ls.count(int(opr1[1]))
		print(numcnt)
	elif(opr1[0]=="quit"):
		exit(0)
	else:
		print("error")

