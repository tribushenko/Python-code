lst = [1, 2, 3, 4, 5, 6]
book = {"title": "The Langoliers",
        "author": "Stephen King",
        "year_published":1990}
string = "Hello, world!"

# for loop
it = iter(lst)
while True:
    try:
        i = next(it)
        #print(i)
    except StopIteration:
        break

from random import random
# Итерируемый объект
class RandomIterator:
    def __iter__(self):
        return self
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

x = RandomIterator(3)
#print(next(x)) # next(x) ~ x.__next__() x -- iterator, когда есть метод __next__

for i in RandomIterator(10):
    print(i)

#iterators
class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration
class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)

for pair in MyList([1,2,3, 4]):
    print(pair)

#end working with iterators

def random_generator(k):
    for i in range(k):
        yield random()

gen = random_generator(3)
# генератор yield в момент запроса next
print(next(gen)) # пока мы не запросим функцию next, то функция не исполняется
print(next(gen)) # отложенное исполнение функции random_generator, то есть функция исполнится, 
# когда нам реально понадобится следующее значение
for i in gen: # итерируем по генератору и выводим три случайных значения 
    print(i)
# когда генератор в функции натыкаются на yield, то генератор прекращает свою работу и бросает исключение StopIteration
def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    return 
    yield 2
    print("Checkpoint 3")

gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(x)
#z = next(gen)

# когда мы добавляем сообщение вместе с return, то это будет сообщением внутри исключения StopIteration
def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    return "No more elements" когда мы добавляем сообщение вместе с return, то это будет сообщением внутри исключения StopIteration
    yield 2
    print("Checkpoint 3")

gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(x)
z = next(gen)

print([(x, y) for x in range(3) for y in range(3) if x >= y]) # генератор списка
z = ((x, y) for x in range(3) for y in range(3) if x >= y) # итератор списка
for i in z: # вызов следующего итератора
    print(i)
