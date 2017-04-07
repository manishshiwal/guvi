str1=raw_input("enter the string")
str2=raw_input("enter the string")
a=256
m = len(str1)
n = len(str2)
if m != n:
	print ("False")
	exit()
mark = [False] * a
map = [-1] * a
for i in range(n):
	if map[ord(str1[i])] == -1:
		if mark[ord(str2[i])] == True:
			print ("False")
		mark[ord(str2[i])] = True
		map[ord(str1[i])] = str2[i]
	elif map[ord(str1[i])] != str2[i]:
		print ("False")
print ("True")
