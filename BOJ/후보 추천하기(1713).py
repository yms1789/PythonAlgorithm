N = int(input())
good_cnt = int(input())
students = list(map(int, input().split()))
picture = []
cnt = []

for i in range(good_cnt):
    if students[i] in picture:
        for j in range(len(picture)):
            if students[i] == picture[j]:
                cnt[j] += 1
    else:
        if len(picture) >= N:
            for j in range(N):
                if cnt[j] == min(cnt):
                    picture.remove(picture[j])
                    cnt.remove(cnt[j])
                    break
        picture.append(students[i])
        cnt.append(1)
picture.sort()
print(" ".join(map(str,picture)))
