x = input().split()

n, k = (int(i) for i in x)
print("using generator( (int(i) for i in ) ): n + k = " + str(n + k))

n, k = map(int, x)
print("using iterator(map): n + k = " + str(n + k))

# lambda functions
even = lambda x : x % 2 == 0
for i in filter(lambda x : x % 2 == 0, (int(i) for i in input().split())):
    print(i)

# sorting by our early defined function
x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]
print(x)
def length(name):
    return len(" ".join(name))

name_lengths = [length(name) for name in x]
print(name_lengths)

x.sort(key = length)
print(x)

#operator library
import operator as op
print("(using operator.add) 5 + 4 = " + str(op.add(5, 4)))
print("(using operator.multiplication) 4 * 5 = " + str(op.mul(4, 5)))
print("if 4 is in [1, 2, 3]: " + str(op.contains([1, 2, 3], 4)))

# op.itemgetter
f1 = op.itemgetter(1) # return the second element of collection
print(f1([1,2,3]))

f2 = op.itemgetter("123")
print(f2({"123": 3, "456":4})) # return the value of the dictionary, which key is "123"

x.sort(key = op.itemgetter(-1))
print(x) # sorting by surname 

f3 = op.attrgetter("sort")
print(f3([1,2,3,4]))

# library functools
from functools import partial
sort_by_last = partial(list.sort, key = op.itemgetter(-1)) # сортировка по последнему элементу(фамилии)
print(x)
sort_by_last(x)
print(x)

y = ["abc", "cba", "abb"] # сортировка по последнему символу в последнем элементе
sort_by_last(y)
print(y)

# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, 
# которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.
mod_checker = lambda x, mod = 0: lambda y: y % x == mod
mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True