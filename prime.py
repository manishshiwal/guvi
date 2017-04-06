n=int(raw_input("enter the number"))
s=0
if(n==1 or n==0):
	print("not prime")
	exit()
for a in range(2,n):
	if(n%a==0):
		s=1
		print("not prime")
		break
if(s==0):
	print("prime")
