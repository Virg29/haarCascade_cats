import hashlib
c=[]
for i in range(2271):
	a = open('./cats/'+str(i)+'.jpg','rb')
	c.append(hashlib.md5(a.read()).hexdigest())
	a.close()
for i in range(2271):
	counter=0
	lastone=0
	lasttwo=0
	for j in range(2271-i):
		if c[i]==c[j+i]:
			counter+=1
			lastone=i
			lasttwo=j+i
	if(counter>1):
		print('--------------')
		print(lastone)
		print(lasttwo)
		print('--------------')