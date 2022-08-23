def solution(records):
    answers = []
    dic = {}
    store = []
    for record in records:
        start_uid = record.find('u')
        uid = record[start_uid:start_uid + 7]
        name = record[start_uid + 8:]
        dic[uid] = name
        if "Enter" in record:
            if uid in store:
                for idx, answer in enumerate(answers):
                    if uid in answer:
                        end_name = answer.find('님')
                        answer = answer.replace(answer[:end_name], name)
                        answers.remove(answers[idx])
                        answers.insert(idx, answer)
                answers.append(dic[uid] + "님이 들어왔습니다.")
            else:
                record = uid + " " + dic[uid] + "님이 들어왔습니다."
                store.append(uid)
                answers.append(record)
        elif "Leave" in record:
            record = uid + " " + dic[uid] + "님이 나갔습니다."
            answers.append(record)
        else:
            for idx, answer in enumerate(answers):
                if uid in answer:
                    end_name = answer.find('님')
                    answer = answer.replace(answer[:end_name], name)
                    answers.remove(answers[idx])
                    answers.insert(idx, answer)
    return answers

def solution2(records):
    answer = []
    dic = {}
    for record in records:
        command = record.split()
        if command[0] == "Enter":
            dic[command[1]] = command[2]
        elif command[0] == "Change":
            dic[command[1]] = command[2]
    for record in records:
        command = record.split()
        if command[0] == "Enter":
            answer.append(f'{dic[command[1]]}님이 들어왔습니다.')
        elif command[0] == "Leave":
            answer.append(f'{dic[command[1]]}님이 나갔습니다.')
    return answer
print(solution(
    ["Enter uid1234 crocat", "Enter uid4567 princess", "Leave uid1234", "Enter uid1234 uter", "Change uid4567 Ryan"]))
