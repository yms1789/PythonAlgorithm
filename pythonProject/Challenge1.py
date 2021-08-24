import sys
import string
input = sys.stdin.readline

a = "map"
# b = ""
#
# print(a)
# for i in a:
#     temp = ord(i)
#     if temp < 97:
#         b = b + ''.join(chr(temp))
#     else:
#         temp += 2
#         if temp > 122:
#             temp -= 26
#             b = b + ''.join(chr(temp))
#             continue
#         b = b + ''.join(chr(temp))
#
# print(b)
before = "abcdefghijklmnopqrstuvwxyz"
after = "cdefghijklmnopqrstuvwxyzab"

key = a.maketrans(before, after)
print(a.translate(key))
