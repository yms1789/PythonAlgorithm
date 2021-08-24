import sys
from collections import deque

input = sys.stdin.readline

expression = input()
digit=''
now=[]
for i in range(len(expression)):
    if expression[i] not in ['+','-']:
        digit+=expression[i]
    else:
        now.append(int(digit))
        now.append(expression[i])
        digit=''
    if i==len(expression)-1:
        now.append(int(digit))
minus=0
res=[now[0]]

for i in range(1,len(now)):
    if now[i]=='-':
        minus+=1
    if type(now[i])==int and minus!=0:
        res.append(-1 * now[i])
    elif type(now[i])==int and minus==0:
        res.append(now[i])
print(sum(res))