# надо заменить все подстроки а на подстроки б в строке с и посчитать через сколько замен в строке с не будет подстрок а

s, a, b = (input() for _ in range(3))
for i in range(10_000):
    s = s.replace(a, b)
    if a in b and a in s:
        print("Impossible")
        break
    elif a not in s and b not in s:
        print(0)
        break
    elif a not in s and b in s:
        print(i + 1)
        break

# найти количество всех вхождений строки t в строку s
s, t = (input() for i in range(2))
count = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        count += 1
print(count)