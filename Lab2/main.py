class deque:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def addFront(self, item):
        self.items.insert(0, item)
    def addRear(self, item):
        self.items.append(item)
    def Front(self):
        return self.items.pop(0)
    def Rear(self):
        return self.items.pop()
class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def empty(self):
        return len(self.items) == 0
    def a(self):
        return self.items


def task1(arr):
    d1 = deque()
    d2 = deque()
    for i in arr:
        d1.addRear(i)
    while d1.size() > 0:
        item = d1.Rear()
        if d2.size() > 1:
            a = d2.Rear()
            while a > item and d2.size() > 0:
               d1.addRear(a)
               a = d2.Rear()
            d2.addRear(min(a, item))
            d2.addRear(max(a, item))
        else:
            d2.addRear(item)
    return d2.items
def task2(str):
    res = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(str)):
        if letters.index(str[i]) != -1:
           res += letters[letters.index(str[i]) - 2]
        else:
            res += str[i]
    return res
def task3(s11, s12, s13, n):
    global s1
    global s2
    global s3
    if(n == 1):
        s13.push(s11.pop())
    else:
        task3(s11, s13, s12, n-1)
        s13.push(s11.pop())
        task3(s12, s11, s13, n-1)
    s1 = s11
    s2 = s12
    s3 = s13
def task4(str):
    s = stack()
    for i in str:
        if i == ")" or i == "(":
            if s.empty():
                s.push(i)
            else:
                a = s.pop()
                if i != ")" and a != "(":
                    s.push(a)
                    s.push(i)
    return s.empty()
def task5(str):
    s = stack()
    for i in str:
        if i == "]" or i == "[":
            if s.empty():
                s.push(i)
            else:
                a = s.pop()
                if i == a:
                    s.push(a)
                    s.push(i)
    return s.empty()
def task6(str):
    s1 = stack()
    s1 = stack()
    for i in str:
        if(i.isdigit()):
            print(i, end = " ")
        elif i.isalpha():
            s1.push(i)
        else:
            s2.push(i)
    while not s1.empty():
        s2.push(s1.pop())
    while not s2.empty():
        s = s2.pop()
        if s.isalpha():
            print(s, end = " ")
        else:
            s1.push(s)
    while not s1.empty():
        print(s1.pop(), end = " ")
    print()
def task7(str):
    d = deque()
    arr = str.split(" ")
    for i in arr:
        if i[0] == '-':
            d.addRear(i)
        else:
            d.addFront(i)
    for i in range(len(arr)):
        a = d.Front()
        if a[0] == '-':
            print(a, end = " ")
        else:
            d.addRear(a)
    while d.size() > 0:
            print(d.Rear(), end = " ")
    print()
def task8(str):
    arr = str.split(". ")
    s = stack()
    for i in arr:
        s.push(i)
    while not s.empty():
        print(s.pop(), end = ". ")

# task1 Выполняем соортировку
file = open("names.txt")
str = file.read()
arr = str.split(", ")
print("task1:")
print(task1(arr))
file.close()
my_file = open("task1.txt", "w+")
for i in task1(arr):
  my_file.write(i + ", ")
my_file.close()

# task2 Выполняем расшифровку
file = open("text.txt")
str = file.read()
print("task2:")
print(task2(str))
file.close()

# task3 ханойские башни
s1 = stack()
s2 = stack()
s3 = stack()
n = 5
for i in range(n, 0, -1):
    s1.push(i)
task3(s1, s2, s3, n)
print("task3:")
print(s3.a())
print(s1.a())

# task4 проверка круглых скобок
file = open("().txt")
str = file.read()
print("task4:")
print(task4(str))
file.close()

# task5 проверка квадратных скобок
file = open("[].txt")
str = file.read()
print("task5:")
print(task5(str))
file.close()\

#task6 сортированная печать
file = open("chars.txt")
str = file.read()
print("task6:")
task6(str)
file.close()

#task7 отрицательные и положительные числа
file = open("nums.txt")
str = file.read()
print("task7:")
task7(str)
file.close()

#task8 строки в обратном порядке
file = open("strings.txt")
str = file.read()
print("task8:")
task8(str)