import re
import requests

num = 63579
while True:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(num)
    response = requests.get(url)
    data = response.text
    if "next nothing is" in data:
        num = re.findall(r"\d+", data)
        num = "".join(num)
        # print(data)
    elif "Divide" in data:
        num = str(int(num)/2)
        # print(num)
    else:
        print(data, num)
        break

#Answer : peak.html