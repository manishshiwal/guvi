n=int(raw_input("enter the number"))
s=0
temp=n
while temp:
  r=temp%10
  s=s+(r*r*r)
  temp/=10
if(s==n):
  print("armstrong")
else:
  print("not armstrong")
