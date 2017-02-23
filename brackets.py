print"WELCOME!!!"
print "Give me a string of brackets"

right= False
dexia = 0
aristeri = 0
string= raw_input()
stringsum=sum(x != '       ' for x in string)
slist= []
for i in string:
    slist.extend(i)
    
for i in range(stringsum):
    if slist[i]=="(":
        dexia+=1
    elif slist[i]==")":
        aristeri +=1
if aristeri == dexia :
    right= True
else :
    right= False
print right 
 

raw_input ("Press <enter> to exit")
