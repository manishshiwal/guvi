n=raw_input("enter the number")
a=list(n)
i=0
while ((i+1)<len(a)):
	a[i],a[i+1]=a[i+1],a[i]
	i+=2
print "".join(a)
