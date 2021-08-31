import re, zipfile

num = str(90052)
comment = ""
f = zipfile.ZipFile('channel.zip')
while True:
    line = f.read(num + ".txt").decode('utf-8')
    new_num = re.findall(r'\d+', line)
    num = "".join(new_num)
    if "nothing is" in line:
        print(line)
        comment = comment + "".join(f.getinfo(num + ".txt").comment.decode('utf-8'))
    else:
        print(line)
        break
print(comment)

#oxygen.html