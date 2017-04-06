n=int(raw_input("enter the number"))
m=int(raw_input("enter the number"))
for x in range(n,m):
	s=0
	temp=x
	while temp:
  		r=temp%10
  		s=s+(r*r*r)
  		temp/=10
	if(s==x):
  		print x
