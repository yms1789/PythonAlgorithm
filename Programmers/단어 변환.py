from collections import deque

def diff(w1, w2):
    diff = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    queue = deque()
    answer = 0
    queue.append((begin, answer))

    if target not in words:
        return 0
    else:
        while queue:
            res = queue.popleft()
            if res[0] == target:
                return res[1]
            for i in range(len(words)):
                if diff(res[0], words[i]) and visited[i] == 0:
                    queue.append((words[i], res[1] + 1))
                    visited[i] += 1

if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))