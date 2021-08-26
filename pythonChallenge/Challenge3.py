import string
import re

f = open("/Users/minsu/PycharmProjects/Challenge3.txt", "r")

str = f.read()
res = ""
code = re.compile("[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]")
reform = re.compile("[A-Z]{3}[a-z]{1}[A-Z]{3}")
rereform = re.compile("[a-z]")

a1 = code.findall(str)
res = ''.join(a1)
a2 = reform.findall(res)
res = ''.join(a2)
a3 = rereform.findall(res)
res = ''.join(a3)
print(res)
