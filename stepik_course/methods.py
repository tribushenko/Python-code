print("cabcd".find("abs")) # индекс начала вхождения подстроки в строку
print("cabcd".find("abc", 1)) # число 1, которое передано в .find() обозначает индекс
# с которого начинать поиск вхождения подстроки в строку

# find - поиск слева, rfind - поиск с правой стороны 
# string.startswith(string, index to start with)
print("QWERTY".lower())

# string.replace(to_replace, replace_with, int first n occurencies to replace)
# string.split()
print("1 2 3 4".split(" ", 2)) # first 2 splits are allowed
print("     1   2   3   4        ".strip().split())

template = "{} is the capital of {}"
print(template.format("London", "Great Britain"))



import requests
template = "Response from {0.url} with code {0.status_code}"

res = requests.get("https://docs.python.org/3.5/")
print(template,format(res))

res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))