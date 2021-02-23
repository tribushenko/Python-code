import requests

f = open("test.txt", "r")
lst = f.read().split("\n")[:-1]
for i in range(len(lst)):
    lst[i] = int(lst[i])
print(lst)
for i in lst:
    res = requests.get(f'http://numbersapi.com/{i}/math?json')
    result = res.json()["found"]
    if result == False:
        print("Boring")
    else:
        print("Interesting")