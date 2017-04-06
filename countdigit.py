a=int(raw_input("enter the number"))
s=0
for n in range(1000):
	if(a):
		r=a%10
		s+=1
		a/=10
print s
