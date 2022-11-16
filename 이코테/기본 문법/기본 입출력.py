import sys

# a = list(map(int, input().split()))
# print(a)

# a, b, c = map(int, input().split())
# print(a, b, c)

# data = sys.stdin.readline().rstrip()
# print(data)

print('정답은 {}'.format(7))


# x = sys.stdin.readline().rstrip()
# if 0 < int(x) < 20:
#     print("0 < x < 20")

def operator(a, b):
    add_var = a + b
    sub_var = a - b
    multiply_var = a * b
    divide_var = a // b
    return add_var, sub_var, multiply_var, divide_var


a, b, c, d = operator(8, 2)
print(a, b, c, d)

print((lambda a, b: a + b)(3, 7))

arr = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]

# 람다 표현식
print(sorted(arr, key=my_key))
print(sorted(arr, key=lambda x: x[1]))

b = list("ABCDE")
print(b)