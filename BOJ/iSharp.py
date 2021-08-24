import sys

input = sys.stdin.readline

str = input()
type, *vals = str.split()
vals = ''.join(vals)

for val in vals.split(','):
    for i in range(len(val)):
        if val[i] == '[' or val[i] == '*' or val[i] == '&' or val[i] == ';':
            name, symbol = val[:i], val[i:]
            break
        else:
            name, symbol = val, ''
    merge = ''
    for i in list(symbol)[::-1]:
        if i == ']':
            merge += '[]'
        elif i == '[':
            continue
        elif i == '*' or i == '&':
            merge += i

    print(type + merge, name + ';')
