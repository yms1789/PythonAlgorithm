# 정수형
a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

# 실수형
a = 157.93
print(a)
a = -1837.2
print(a)
a = -.7
print(a)

a = 1e9
print(a)  # 10억

a = 75.25e1
print(a)  # 752.5

a = 3954e-3
print(a)  # 3.954

a = round((0.3 + 0.6), 4)
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 7
b = 3
# 나누기
print(a / b)

# 나머지 연산
print(a % b)

# 몫
print(a // b)

# 거듭 제곱
print(a ** b)
print(a ** 0.5)

# 리스트 자료형
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)  # [0,0,0,0,0,0,0,0,0,0]

print(a[1:4])

# 리스트 컴프리헨션
arr = [i for i in range(10)]
print(arr)

arr = [i for i in range(10) if i % 2 == 1]
print(arr)  # [1, 3, 5, 7, 9]

# remove_set에 들어있는 값을 a에서 전부 제거
a = [1, 2, 3, 4, 5, 5, 5]

remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

data = "Don't you know \"Python\""
print(data)

# 문자열 연산
a, b = ("Hello", "World")
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2:4])

# 사전 자료형
data = dict()
data['사과'] = 'APPLE'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print('사과 데이터 존재')

# 집합 자료형
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
data = {1, 2, 3, 4, 1, 2, 3, 4}
print(data)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a | b)
print(a & b)
print(a - b)
