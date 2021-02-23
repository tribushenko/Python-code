# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.

# В следующих n строках содержится описание наследования классов. В i-й строке указано
# от каких классов наследуется i-й класс.
# Обратите внимание, что класс может ни от кого не наследоваться.
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
# что класс не наследуется явно от одного класса более одного раза.

# В следующей строке содержится число q - количество запросов.

# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes",
# если класс 1 является предком класса 2, и "No", если не является.

# ****************************Тест  № 1****************************
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A
# ****************************Тест № 2****************************
# 11
# Obj
# A : Obj
# B : Obj
# C : Obj
# F : A
# K : A B
# Z : B
# G : C
# L : F K
# N : G
# P : L Z N
# 13
# A K
# A A
# Obj B
# B P
# N G
# G L
# Z P
# P Z
# Obj k
# K B
# K C
# G Z
# N P


def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path += [start]
    if start == end:
        return True
    if start not in graph.keys():
        return False
    for node in graph.get(start):
        if node not in path:
            new_node = dfs(graph, node, end, path)
            if new_node:
                return new_node
    return False


graph = dict()
for i in range(int(input())):
    inherit = input().split(":")
    if len(inherit) != 1 and inherit[0][:-1] in graph.keys():
        for parent in inherit[1].split():
            graph[inherit[0][:-1]].append(parent)
    else:
        if len(inherit) == 1:
            graph[inherit[0]] = "object"
        else:
            graph[inherit[0][:-1]] = inherit[1].split()

for i in range(int(input())):
    end, start = input().split()
    value = dfs(graph, start, end)
    print("Yes" if value == True else "No")
