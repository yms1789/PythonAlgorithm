# 순열
from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)  # data중 3개를 뽑는 모든 순열이 출력됨

# 조합
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)  # data 중 2개를 뽑는 모든 조합이 출력됨

data = ['A', 'B', 'C']  # 데이터 준비
result = list(product(data, repeat=2))
# 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)


data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
# 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)
