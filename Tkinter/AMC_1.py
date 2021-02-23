import tkinter
import random
import math
from PIL import ImageTk, Image
import os

root = tkinter.Tk()
root.geometry("800x800")
root.title("Головне вікно")

class number_equals_zero(Exception):
    pass

# Лінійний алгоритм
def LinearAlgo():
    lin = tkinter.Toplevel(root)
    lin.geometry("800x800")
    lin.title("Лінійний алгоритм")
    tkinter.Label(lin, text="Аргументи a, b, c можна задати рандомно", font="Arial 13 bold", bg="green").place(relx=0.2, rely=0.05)
    tkinter.Label(lin, text="або власноруч", font="Arial 13 bold", bg="green").place(relx=0.4, rely=0.09)
    a, c, s, d = (0 for i in range(4))
    b = -1
    def randomABC():
        global a, b, c, s, d
        a = random.randrange(-5, 5)
        b = random.randrange(1, 10)
        c = random.randrange(-5, 5)
        s = random.randrange(1, 5)
        d = random.randrange(1, 5)
        tkinter.Label(lin, text=f"a = {a}\nb = {b}\nc = {c}\ns = {s}\nd = {d}", font="Arial 12 bold", width = 15, height=12).place(relx=0.6, rely=0.3)
        return (a, b, c, s, d)
        
    def manualABC():
        try:
            global a, b, c, s, d
            a = int(entry_a.get("1.0",'end-1c'))
            b = int(entry_b.get("1.0",'end-1c'))
            s = int(entry_s.get("1.0",'end-1c'))
            d = int(entry_d.get("1.0",'end-1c'))
            if b == 0 or s == 0 or d == 0:
                b = -1000000
                s = -1000000
                d = -1000000
                raise number_equals_zero
            c = int(entry_c.get("1.0",'end-1c'))
            tkinter.Label(lin, text=f"a = {a}\nb = {b}\nc = {c}\ns = {s}\nd = {d}", font="Arial 12 bold", width=15, height=12).place(relx=0.6, rely=0.3)
        except ValueError:
            tkinter.messagebox.showinfo(title="ValueError", message="Введіть тип даних, який відповідає числу, а не рядку!")
        except number_equals_zero:
            tkinter.messagebox.showinfo(title="number_equals_zero", message="Введіть число b, яке не дорівнює 0!")
        return (a, b, c, s, d)
            
    def getResults():
        global a, b, c, s, d
        res = tkinter.Toplevel(lin)
        res.geometry("900x200")
        res.title("Обрахунки")
        tkinter.Label(res, text="Формула: Y1 = s^(a/b + c) + d^(a/b + c)", font="Arial 12 bold").place(relx=0.2, rely=0.05)
        #print(a, b, c, d, s)
        result = s**(a/b + c) + d**(a/b + c)
        print(result)
        if type(result) == complex:
            tkinter.Label(res, text=f"Результат - комплексне число: Y1 = {result}", font="Arial 11 ", fg="red").place(relx=0.01, rely=0.5)
        else:
            tkinter.Label(res, text=f"Результат: Y1 = {result}", font="Arial 13 bold ", fg="red").place(relx=0.01, rely=0.5)    
    # Ввод а
    tkinter.Label(lin, text="Введіть а: ", font="Arial 12 bold").place(relx=0.1, rely=0.12)
    entry_a = tkinter.Text(lin, width=25, height=2)
    entry_a.place(relx=0.1, rely=0.15)
    # Ввод b
    tkinter.Label(lin, text="Введіть b: ", font="Arial 12 bold").place(relx=0.1, rely=0.2)
    entry_b = tkinter.Text(lin, width=25, height=2)
    entry_b.place(relx=0.1, rely=0.23)
    # Ввод с
    tkinter.Label(lin, text="Введіть c: ", font="Arial 12 bold").place(relx=0.1, rely=0.28)
    entry_c = tkinter.Text(lin, width=25, height=2)
    entry_c.place(relx=0.1, rely=0.31)
    # Ввод s
    tkinter.Label(lin, text="Введіть s: ", font="Arial 12 bold").place(relx=0.1, rely=0.36)
    entry_s = tkinter.Text(lin, width=25, height=2)
    entry_s.place(relx=0.1, rely=0.39)
    # Ввод d
    tkinter.Label(lin, text="Введіть d: ", font="Arial 12 bold").place(relx=0.1, rely=0.44)
    entry_d = tkinter.Text(lin, width=25, height=2)
    entry_d.place(relx=0.1, rely=0.47)
    # Рандомные a, b, c
    randomButton = tkinter.Button(lin, text="Задати a, b, c рандомно", font="Arial 13 bold", command=randomABC)
    randomButton.place(relx=0.45, rely=0.2)
    # считывание a, b, c, s, d
    buttonRead = tkinter.Button(lin, text="Задати числа власноруч", font="Arial 13 bold", command=manualABC)
    buttonRead.place(relx=0.1, rely=0.53)
    # Получить результаты подсчёта
    tkinter.Label(lin, text="Отримати результати:", font="Arial 13 bold").place(relx=0.1, rely=0.62)
    buttonGetResults = tkinter.Button(lin, text="Провести обрахунки і отримати результати", font="Arial 13 bold", fg="red", command=getResults)
    buttonGetResults.place(relx=0.1, rely=0.65)
# Розгалуження
def BranchAlgo():
    branch = tkinter.Toplevel(root)
    branch.geometry("800x800")
    branch.title("Алгоритм розгалуження")
    tkinter.Label(branch, text="Аргумент х можна задати рандомно", font="Arial 13 bold", bg="green").place(relx=0.2, rely=0.05)
    tkinter.Label(branch, text="або власноруч", font="Arial 13 bold", bg="green").place(relx=0.4, rely=0.09)
    x = 1
    def randomX():
        global x
        x = random.randrange(-10, 10)
        tkinter.Label(branch, text=f"x = {x}", font="Arial 12 bold", width = 10, height=5, bg="red").place(relx=0.6, rely=0.2)
        return x
    
    def manualX():
        global x
        x = int(entry_x.get("1.0",'end-1c'))
        tkinter.Label(branch, text=f"x = {x}", font="Arial 12 bold", width = 10, height=5, bg="red").place(relx=0.6, rely=0.2)
        return x

    def getResults():
        try:
            global x
            if x > 0:
                tkinter.Label(branch, text="Так як x > 0", font="Arial 12 bold").place(relx=0.26, rely=0.55)
                tkinter.Label(branch, text="формула: у = cos(x)/sin(x) + (sin(x))^1/3", font="Arial 12 bold").place(relx=0.26, rely=0.6)
                result = math.cos(x)/math.sin(x) + math.pow(math.sin(x), -3)
            elif x == 0:
                tkinter.Label(branch, text="Так як x = 0", font="Arial 12 bold").place(relx=0.26, rely=0.55)
                tkinter.Label(branch, text="формула: у = (cos(x))^2 / 0.15", font="Arial 12 bold").place(relx=0.26, rely=0.6)
                result = math.pow(math.cos(x), 2) / 0.15
            else:
                tkinter.Label(branch, text="Так як x < 0", font="Arial 12 bold").place(relx=0.26, rely=0.55)
                tkinter.Label(branch, text="формула: у = cos(x)/sin(x) + (cos(x))^1/3", font="Arial 12 bold").place(relx=0.26, rely=0.6)
                result = math.cos(x)/math.sin(x) + math.pow(math.cos(x), -3)
            tkinter.Label(branch, text=f"Результат: у = {result}", font="Arial 12 bold", fg="red").place(relx=0.26, rely=0.65)
        except NameError:
            tkinter.messagebox.showinfo(title="NameError", message="Введіть спочатку х")
            pass
    # х задаётся рандомно
    randomButton = tkinter.Button(branch, text="Задати x рандомно", font="Arial 13 bold", command=randomX)
    randomButton.place(relx=0.55, rely=0.4)
    # x задаётся с клавиатуры
    tkinter.Label(branch, text="Введіть x: ", font="Arial 12 bold").place(relx=0.1, rely=0.2)
    entry_x = tkinter.Text(branch, width=25, height=2)
    entry_x.place(relx=0.1, rely=0.23)
    buttonReadX = tkinter.Button(branch, text="Задати х власноруч", font="Arial 12 bold", command=manualX)
    buttonReadX.place(relx=0.07, rely=0.26)
    # Посчитать результаты
    buttonResult = tkinter.Button(branch, text="Отримати результати", font="Arial 13 bold", command=getResults)
    buttonResult.place(relx=0.3, rely=0.45)
# Циклічний алгоритм
def LoopAlgo():
    loop = tkinter.Toplevel(root)
    loop.title("Циклічний алгоритм")
    loop.geometry("900x400")
    m = 45
    global way
    way = ""
    def manual_generation():
        global way
        way = "manual"
    def random_generate():
        global way
        way = "random"
    def compute():
        print(way)
        res = tkinter.Toplevel(loop)
        res.title("Результат обчислень")
        res.geometry("700x300")
        numerator = 1
        denominator = 0
        if way == "random":
            for i in range(m):
                numerator *= random.randrange(1, 3)
                denominator += random.randrange(1, 50)
        elif way == "manual":
            num = [int(i) for i in entry_num.get("1.0",'end-1c').split(" ")]
            den = [int(i) for i in entry_denom.get("1.0",'end-1c').split(" ")]
            for i in num:
                numerator *= i
            for i in den:
                denominator += i
        print(numerator, denominator)
        tkinter.Label(res, text="Результат обчислень: f = {0}".format(round(numerator/denominator, 2)), font="Arial 15 bold", fg="red").place(relx=0.1, rely=0.1)
        
    tkinter.Label(loop, text="Оберіть спосіб,", font="Arial 12 bold", fg="red").place(relx=0.33, rely=0.05)
    tkinter.Label(loop, text="яким будуть генеруватися чисельника та знаменник", font="Arial 12 bold", fg="red").place(relx=0.07, rely=0.1)
    tkinter.Label(loop, text="Ввести числа чисельника власноруч через пробіл: ", font="Arial 12 bold").place(relx=0.1, rely=0.24)
    entry_num = tkinter.Text(loop, width=45, height=2)
    entry_num.place(relx=0.3, rely=0.3)
    tkinter.Label(loop, text="Ввести числа знаменника власноруч через пробіл: ", font="Arial 12 bold").place(relx=0.1, rely=0.38)
    entry_denom = tkinter.Text(loop, width=45, height=2)
    entry_denom.place(relx=0.3, rely=0.45)
    button_read = tkinter.Button(loop, text="↑Зчитати числа знаменника та чисельника↑", font="Arial 12 bold", command=manual_generation)
    button_read.place(relx=0.1, rely=0.55)
    buttonRandom = tkinter.Button(loop, text="Згенерувати числа чисельника та знаменника \nрандомно", font="Arial 13 bold", command=random_generate)
    buttonRandom.place(relx=0.05, rely=0.64)    
    buttonResult = tkinter.Button(loop, text="Порахувати циклічним алгоритмом", font="Arial 13 bold", fg="red", command=compute)
    button_result = tkinter.Button(loop, text="Вивести результат", font="Arial 14 bold", fg="red", command=compute)
    button_result.place(relx=0.25, rely=0.8)

    
    

        
tkinter.Label(root, text="Доброго дня! Лабораторна № 1 з АМО", font="Arial 15 bold").place(relx=0.15, rely=0.5)
tkinter.Label(root, text="Роботу виконав студент ІВ-93", font="Arial 15 bold").place(relx=0.2, rely=0.6)
tkinter.Label(root, text="Трибушенко Артем", font="Arial 15 bold", fg="red").place(relx=0.35, rely=0.7)
tkinter.Label(root, text="Варіант № 27", font="Arial 15 bold").place(relx=0.4, rely=0.8)
buttonLinear = tkinter.Button(root, text="Лінійний", font="Arial 12 bold", command=LinearAlgo)
buttonIf = tkinter.Button(root, text="Що розгалужується", font="Arial 12 bold", command=BranchAlgo)
buttonLoop = tkinter.Button(root, text="Циклічний", font="Arial 12 bold", command=LoopAlgo)
buttonLinear.place(relx = 0.1, rely = 0.1)
buttonIf.place(relx=0.30, rely=0.1)
buttonLoop.place(relx=0.7, rely=0.1)

root.mainloop()
