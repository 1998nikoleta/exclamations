print "WELLCOME!!! Give me a list of numbers including zeros"
print "Note: Seperate them with <space>"
seperate = raw_input()
numlist= map(int, seperate.split())
position = 0
for i in range(len(numlist)):
    if numlist[i] != 0:
        numlist[position] = numlist[i]
        position += 1

for i in reversed(range(position, len(numlist))):
    numlist[i] = 0

print numlist

raw_input("Press <enter> to exit")
