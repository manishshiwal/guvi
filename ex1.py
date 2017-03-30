print "hello guys"
print """this is paragraph not a sngh;e lin
this is secong line """
a=10
b=20
print "sum=",a+b
def plus (a,b):
 print"funtion sum= a+b"
 return a+b
print plus(a,b)
print
print
ten_things="Apples Oranges Crows Telephone Light Sugar"
print "wait there'snot 10 things in that lost, let's fix that."
stuff=ten_things.split(' ')
more_stuff=["day","night",'song','frisbee','corn','banana','girl','boy']
while len(stuff)!=10:
 next_one=more_stuff.pop()
 print "adding:",next_one
 stuff.append(next_one)
 print "there's %i items now"%len(stuff),35+15
print "there we go",stuff
print "let's do some thing with stuff"
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print'#'.join(stuff[3:5])
print stuff[-2]
print stuff[-1]
print
print
for cat in stuff:
 print cat
print
print
states={"help":'rock',"lol":"hehe",1:"one",2:"two"}
print states
print
print states[1]
print
print states["help"]
print
states[3]="three"
print states
print
state=states.get("four",None)
print state
import apple
apple.apples()
print apple.abc
