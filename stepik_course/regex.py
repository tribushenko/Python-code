import re 

# сырая строка в пайтоне - которая выводит всё без строковых литералов
a = r"Heelo\n\tWorld"
print(re.match) # берёт шаблон и нашу строку и проверяет подходит ли данная строка под данный шаблон
                # Этот метод ищет по заданному шаблону в начале строки. 
print(re.search) # берёт нашу строку и находит первую подстроку, которая подходит под наш шаблон
print(re.findall) # находит все подстроки нашей строки, который подходит под данный шаблон
print(re.sub) # позволяет заменить все вхождения подстрок, которые подходят под наш шаблон чем-нибудь другим 

# --------------элементарные регулярки без метасимволов------------------------
pattern = r"abc"
string = "abcd"
match_object = re.match(pattern, string) 
print(match_object) # span отображает от какого и к какому индексу находится pattern в string
                    # match отображает паттерн, который мы хотели найти
pattern = r"abc"
string = "accd"
match_object = re.match(pattern, string) # если pattern всё таки нет в string, то re.match 
                                         # возвращает None 
print(match_object) 

string = "babc"
search_object = re.search(pattern, string) # числа, которые вернулись в span - те же самые при срезе
print(search_object)

#----------------------------регулярки с перечислениями среднего символа (или то, или то)--------------------- 
# [] -- можно указать множество подходящих символов
pattern = r"a[abc]c" # в [] лежит символы, которые могут быть использованы в re.match (або а, або b, або с)
string = "aac" # or abc, or acc
match_object = re.match(pattern, string)
print(match_object)

# работа функции re.findall() - все включение нашего паттерна в строку string
string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# работа функции re.sub() - заменяет все включения нашего паттерна на указанный аргумент внутри re.sub()
fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
 
# -------------------------------------продвинутые метасимволы-------------------------------------
# основные мета-символы -- . ^ $ * + ? { } [ ] \ | ( ) 
pattern = " english?" # не сработает так, как нужно заэкранировать знак вопроса
pattern = "english\?" # это сработает так, как мы заекранировали вопросительный знак
string = "Do you speak english?" 
match = re.search(pattern, string)
print(match)

# [a-d] -- символы от а до d
pattern = r"a[a-d]c"
string = "acc"
match_object = re.match(pattern, string) # сработает так, как посредине все символы от а до d
print(match_object)

# поиск всех включений pattern, средний символ есть от a до d, в string.   
string = "abc, acc, aac, adc"
all_inclusions = re.findall(pattern ,string)
print(all_inclusions)

# замена всех string, которые соответствуют паттерну на "abc"
fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

# -----------------средний элемент может быть в диапазоне всех букв латинского алфавита-------------------
pattern = "a[a-zA-Z]c"
string = "acc"
match_object = re.match(pattern, string)
print(match_object)

string = "abc, acc, aac, adc, aZc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

# ----------------средний элемент не может быть в диапазоне всех букв латинского алфавита----------------
pattern = "a[^a-zA-Z]c"
string = "acc"
match_object = re.match(pattern, string)
print(match_object)

string = "ac, a2c, a*c, adc, acc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

# сокращения некоторых выражений
"""
\d ~ [0-9] -- цифры
\D ~ [^0-9] -- цифры
\s ~ [ \t\n\r\f\v] -- пробельные символы (в начале - пробел)
\S ~ [^ \t\n\r\f\v]
\w ~ [a-zA-Z0-9_] -- буквы + цифры + _(нижнее подчёркивание) 
\W ~ [^a-zA-Z0-9_]
"""
pattern = r"a.c" # паттерн, который начинается на а, заканчивается на с и между ними любой символ
pattern = r"a[\w.]c" # паттерн, который допускает все буквы, цифры, нижнее подчеркивание и точку 

# ----метасимвол -- * обозначает любое количество символов на этом месте в том числе и 0 символов---------------------------
pattern = r"ab*a" # любое количество символов b на месте звёздочки или их отсутствие
pattern = r"ab+a" # любое количество символов b на месте звёздочки не менее одного
pattern = r"ab?a" # ноль либо одно вкхождение символа b
pattern = r"ab{3}a" # элементы, в которых ровно три вхождения b
pattern = r"ab{1,2}a" # элементы, в которых от одного до двух вхождений b    
string = "aa, aba, abba"
print(re.findall(pattern, string))

# регулярные выражения работают жадным образом, то есть имея 
pattern = r"a[ab]+a" # любое количество символов b на месте звёздочки не менее одного
string = "abababababaa" # вернёт всю строку, а не к примеру первые три символа
print(re.match(pattern, string))
# чтобы этого избежать нужно добавить знак вопроса (?) после +
# чтобы алгоритм работал не жадно
pattern = r"a[ab]+?a"  
string = "abababababaa"
print(re.match(pattern, string))

# --------------------------мы можем группировать символы---------------------------------
pattern = r"(test)*" # для группировки используем круглые скобки ()
string = "testtest"
match = re.match(pattern, string)
print(match)


pattern = r"(test|text)*" # или то, или иное
string = "testtext"
match = re.match(pattern, string)
print(match)

pattern = r"abc|(test|text)*" # либо abc, либо всё оставшееся выражение (test|text)*
string = "testtext"
string = "abc"
match = re.match(pattern, string)
print(match)

pattern = r"((abc)|(test|text)*)" # три группы - полностью всё выражение, abc, всё оставшееся выражение (test|text)*
string = "abc"
string = "testexttest" # последнее вхождение test в string
match = re.match(pattern, string)
print(match)
print(match.groups()) # match.groups(index) - index элемента списка match.groups()

pattern = r"(\w+)-\1" # собрать группу из цифер, букв и нижнего подчеркивания и через тире найти ещё такую самую группу
string = "test-test" # \1 - первая группа (группа, открывающая скобки), а если \3 - третья группа (группа, открывающая третью скобку)
match = re.match(pattern, string)
print(match)

# ------------------------------re.sub()----------------------------------------
pattern = r"(\w+)-\1" 
string = "test-test chow-chow"
match = re.sub(pattern, r"\1", string) # оставить только первую группу оставив только test и chow
print(match)

# -------------------------------re.findall()-----------------------------------
pattern = r"((\w+)-\2)" 
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates)

# -----------------------------ignoring case of text-----------------------------
x = re.match(r"text", "TEXT", re.IGNORECASE)
print(x)

x = re.match(r"(te)*xt", "TEXT", re.IGNORECASE | re.DEBUG) # -- максимальное кол-во вхождений pattern
# r"(te)*?xt - минимальное кол-во вхождений"
print(x)