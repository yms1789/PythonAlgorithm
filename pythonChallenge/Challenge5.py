import requests
import pickle
import urllib.request

response = requests.get("http://www.pythonchallenge.com/pc/def/{}.{}".format("banner", "p"))

data = pickle.loads(response.content)
# print(data)

for line in data:
    res = ""
    for i in range(len(line)):
        char = line[i][0] # res에 넣을 문자
        for i in range(line[i][1]): # 횟수
            res += char
    print(res)
