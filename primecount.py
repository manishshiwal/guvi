a=int(raw_input("enter the number"))
b=int(raw_input("enter the number"))
c=0
if(a==1 or a==0):
	a=2
for n in range(a,b):
	s=0
	for x in range(2,n):
		if(n%x==0):
			s=1
			break
	if(s==0):
		c+=1
print c
