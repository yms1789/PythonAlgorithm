def solution(new_id):
    answer = ''
    new_id = new_id.lower()  # 1

    for word in new_id:  # 2
        if word.isalnum() == True or word in '-._':
            answer += word

    while '..' in answer:  # 3
        answer = answer.replace('..', '.')

    answer = answer.rstrip('.').lstrip('.') # 4

    if len(answer) == 0:
        answer = "a"

    if len(answer) >= 16: # 6
        answer = answer[0:15]
        answer = answer.rstrip('.')

    elif len(answer) <= 2: # 7
        while len(answer) != 3:
            answer += answer[-1]
    return answer
if __name__=="__main__":
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))
