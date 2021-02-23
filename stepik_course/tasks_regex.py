import sys
import re 

# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
'''for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = r"(.*cat.*){2}"
        match = re.search(pattern, line)
        if match:
            print(line)
    else:
        break'''

# Выведите строки, содержащие "cat" в качестве слова.
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = r"\bcat\b" 
        search = re.search(pattern, line)
        if search:
            print(line)
    else:
        break"""

# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = r"z.{3}z"
        search = re.search(pattern, line)
        if search:
            print(line)
    else:
        break"""

# Выведите строки, содержащие обратный слеш "\".
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = r"\\"
        search = re.search(pattern, line)
        if search:
            print(line)
    else:
        break"""

# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор). 
# Пример - blabla is a tandem repetition
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = r"\b(\w+)\1\b"
        search = re.search(pattern, line)
        if search:
            print(line)
    else:
        break"""

# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = "human"
        sub = re.sub(pattern, "computer", line)
        if sub:
            print(sub)
    else:
        break"""

# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = r"\ba+\b"
        sub = re.sub(pattern, "argh", line, count = 1, flags=re.IGNORECASE)
        if sub:
            print(sub)
    else:
        break"""

# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = r"\b(\w)(\w)(\w*)\b"
        sub = re.sub(pattern, r"\2\1\3", line)
        if sub:
            print(sub)
    else:
        break"""

# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
"""for line in sys.stdin:
    line = line.rstrip()
    if line:
        pattern = "(\w+)(\w*)"
        sub = re.sub(pattern, r"\1", line)
        if sub:
            print(sub)
    else:
        break"""

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\A[01]+\Z",line):
         if re.fullmatch(r"REG-EXP",line[::-1]):
             print(line)