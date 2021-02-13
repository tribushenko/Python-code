# В первой строке входных данных содержится целое число n - число классов исключений.
# В следующих n строках содержится описание наследования классов. В i-й строке указано
# от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться.
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
# что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.

# 4
# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError

def dfs(graph, exception, banned):
    for key, value in graph.items():
        if exception == key:
            for i in value:
                banned.add(i)
                dfs(graph, i, banned)
    return banned
graph = dict()
for i in range(int(input())):
    inherit = input().split(":")
    if len(inherit) != 1:
        for parent in inherit[1].split():
            for child in inherit[0].split():
                if parent in graph.keys():
                    graph[parent].append(child)
                else:
                    graph[parent] = [child]
banned = set()
for i in range(int(input())):
    exception = input()
    if exception in banned:
        print(exception)
    else:
        dfs(graph, exception, banned)

