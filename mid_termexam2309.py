#question1
from sys import argv
script,n=argv
result=0
for i in range(2,n+1):
    result += (i-1)/i
print(result)


