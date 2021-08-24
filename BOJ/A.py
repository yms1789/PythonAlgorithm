import sys
from itertools import combinations

input = sys.stdin.readline
vowels = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())  # L = 암호 구성하는 알파벳 갯수 C = 입력받는 문자 갯수
passwd = list(map(str, input().split()))
output_passwd = []
passwd.sort()
res = list(combinations(passwd, L))

def count(res):
    for password in res:
        cons = 0
        vowel = 0
        for alpha in password:
            if alpha in vowels:
                vowel += 1
            else:
                cons += 1
        if cons >= 2 and vowel >= 1:
            print("".join(password))
    return

count(res)
