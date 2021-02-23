import requests
import re

A = input()
B = input()
pattern = r"https://stepic.org/media/attachments/lesson/24472/.+.html"

def find(link):
    return True if B in re.findall(pattern, requests.get(link).text) else False

findall = re.findall(pattern, requests.get(A).text)
flag = False
for i in findall:
    if find(i) == True:
        flag = True
if flag == False:
    print("No")
else:
    print("Yes")


link = input().strip()
needed = list(set(re.findall(r"(?:\<a.*\bhref=)(?:[\s\"'])?(?:\w+://)?([\w.-]+)(?:.*>)", requests.get(link).text)))
needed.sort()
for i in needed:
    if i != "..":
        print(i)