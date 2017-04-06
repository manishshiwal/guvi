a=int(raw_input("enter the number"))
if(a%4==0):
	if(a%100!=0):
		print("leap year")
	elif(a%400!=0):
		print("not a leap year")
	else:
		print("leap year")
else:
	print("not a leap year")
