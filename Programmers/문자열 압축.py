def solution(s):
    res = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        div = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    div += str(cnt) + tmp
                else:
                    div += tmp
                tmp = s[j:j + i]
                cnt = 1
        if cnt != 1:
            div += str(cnt) + tmp
        else:
            div += tmp
        res.append(len(div))

    return min(res)


if __name__ == "__main__":
    s = "abcabcdede"
    print(solution(s))
