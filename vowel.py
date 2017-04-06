n=raw_input("enter the letter")
ab=['a','A','e','E','i','O','u','o','I','U']
b=1
for c in ab:
	if(n==c):
  		print("vowel")
  		b=0
if(b==1):
  print("consonant")
