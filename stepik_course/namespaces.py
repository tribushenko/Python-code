# Программа реализует поведение namespace в языке Python
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> 
# при запросе из пространства <namespace>, или None, если такого пространства не существует

#Sample Input:

#9
#add global a
#create foo global
#add foo b
#get foo a
#get foo c
#create bar foo
#add bar a
#get bar a
#get bar b

#Sample Output:

#global
#None
#bar
#foo

varies_dict, funcs_dict = {}, {}
def create(namespace, variable):
    if namespace in funcs_dict:
        funcs_dict[namespace] += variable
    else:
        funcs_dict[namespace] = variable
    return funcs_dict
def add(namespace, variable):
    if namespace not in varies_dict:
        varies_dict[namespace] = [variable]
    else:
        varies_dict[namespace] += [variable]
def get(variable, namespace):
    try:
        if variable in varies_dict[namespace]:
            return namespace
        else:
            return get(variable, namespace = funcs_dict[namespace])
    except KeyError:
        try:
            return get(variable, namespace = funcs_dict[namespace])
        except KeyError:
            return None
n = int(input())
for i in range(n):
    cmd, namespace, variable = input().split()
    if cmd == "add":
        add(namespace, variable)
    elif cmd == "create":
        create(namespace, variable)
    else:
        print(get(variable, namespace))
