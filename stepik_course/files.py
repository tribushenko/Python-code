f = open("test.txt", "r") # первый аргумент - имя файла, второй - то, как мы открываем эти данные
# r - read(default)
# w - write содержимое файла стирается и записываются новые данные
# a - append запись ведётся в конец
# b - binary открыть в бинарном режиме
# t - text открыть в текстовом режме(по умолчанию) 
# r+ - открыть для чтения и записи 
# w+ - открыть для чтения и записи, данные файла стираются
x = f.read(5) # чтение первых пяти символов
print(x)
y = f.read()
print(y)
f.close()

print("\n methods for reading a file \n")
f = open("test.txt", "r")
x = f.readline() # есть ещё метод read(), который считывает содержимое всего файла, но readline считывает построчно 
x = x.rstrip() # убирает все пробельные символы с правой стороны в строчке или применить сразу к readline()
x = x.splitlines() # сплитит построчно и каждую строку определяет как элемент списка
print(repr(x)) # представление данных в файле символьно
f.close()

# \nfor
print("\n for loop \n") 
f = open("test.txt", "r")
for line in f:
    line = line.rstrip()
    print(repr(line))
x = f.read() # после окончания считывания пайтон будет считывать пустую строку и печатать её
print(x + " ------ empty line")
f.close()

# --------------writing lines to the file ------------- 
f = open("test1.txt", "w")
f.write("Hello\n")
f.write("world")
lines = ["Line 1", "Line 2", "Line 3"]
to_write = "\n".join(lines)
f.write(to_write)
f.close()

# альтернатива f.open() & f.close()
with open("test.txt") as f, open("testCopy.txt", "w") as w:
    for line in f:
        w.write(line)

