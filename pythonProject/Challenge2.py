from collections import Counter

f = open("/Users/minsu/a.txt", "r")

line = f.read()
print(Counter(line))

