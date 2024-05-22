import random
import timeit
import copy
#Бинарный поиск
def binary(mas, a):
    l = 0
    r = len(mas)-1
    m = int((l + r) / 2)
    while mas[m] != a and r - l > 1:
        if mas[m] > a:
            r = m
        else:
            l = m
        m = int((l + r) / 2)
    if mas[r] == a:
        m = r
    if mas[m] == a:
        return m
    else:
        return -1
#Добавить в массив
def add(mas):
    a = (int)(input("Введите число которого хотите добавить:"));
    masRes = [i for i in mas]
    masRes.append(a)
    return masRes
#Сгенерировать массив
def generateMas():
    import random
    length = int(input("Введите длину массива:"))
    min = int(input("Введите минимальное число в массиве:"))
    max = int(input("Введите максимальное число в  массиве:"))
    masRes = [random.randint(min, max) for _ in range(length)]
    masRes.sort()
    print(masRes)
    return masRes
#Удалить элемент с массива
def delete(mas):
    a = (int)(input("Введите число которого хотите удалить:"));
    mas.remove(a)
    return mas
#Класс узла
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
#Класс дерева
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)
    def _insert(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)
    def search(self, key):
        return self._search(key, self.root)
    def _search(self, key, node):
        if node is None or node.val == key:
            return node
        elif key < node.val:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)
    def _find_min(self, node):
        if node.left:
            return self._find_min(node.left, node)
        else:
            return node

    def delete(self, key):
        self.root = self._delete(key, self.root)
    def _delete(self, key, node):
        if node is None:
            return node
        elif key < node.val:
            node.left = self._delete(key, node.left)
        elif key > node.val:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right = self._delete(min_node.val, node.right)
        return node
    def printTree(self):
        result = []
        self._printTree(self.root, result)
        return result
    def _printTree(self, node, result):
        if node is not None:
            self._printTree(node.left, result)
            result.append(node.val)
            self._printTree(node.right, result)
#Фибоначиев поиск
def fibonachi_search(arr, x):
    fib1, fib2 = 0, 1
    while fib2 < len(arr):
        fib1, fib2 = fib2, fib1 + fib2
    offset = -1
    while fib2 > 1:
        i = min(offset + fib1, len(arr) - 1)
        if arr[i] < x:
            fib2, fib1 = fib1, fib2
            fib1 = fib2 - fib1
            offset = i
        elif arr[i] > x:
            fib2 = fib1
            fib1 = fib2 - fib1
        else:
            return i
    if fib1 and offset < len(arr) - 1 and arr[offset + 1] == x:
        return offset + 1
    return 'В массиве нет элемента с таким значением'
#Интерполяционный поиск
def interpolation_search(arr, item):
    low, high = 0, len(arr) - 1
    while low <= high and item >= arr[low] and item <= arr[high]:
        pos = low + ((item - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == item:
            return pos
        elif arr[pos] < item:
            low = pos + 1
        else:
            high = pos - 1
    return None
#Простое рехэширование
class HashTableP:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size
    def hashFunction(self, key):
        return key % self.size
    def put(self, key, data):
        index = self.hashFunction(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = data
        else:
            while self.keys[index] is not None:
                if self.keys[index] == key:
                    self.values[index] = data
                    return
                index = (index + 1) % self.size
            self.keys[index] = key
            self.values[index] = data
    def get(self, key):
        index = self.hashFunction(key)
        if self.keys[index] is None:
            return None
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None
#Метод цепочек
class HashTableZ:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.buckets = [None] * self.capacity
    def add(self, key, value):
        index = hash(key) % self.capacity
        node = self.buckets[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1
        if self.size > 0.7 * self.capacity:
            self.resize()
    def get(self, key):
        index = hash(key) % self.capacity
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None
    def remove(self, key):
        index = hash(key) % self.capacity
        node = self.buckets[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return
            prev = node
            node = node.next
    def resize(self):
        new_capacity = self.capacity * 2
        new_buckets = [None] * new_capacity
        for i in range(self.capacity):
            node = self.buckets[i]
            while node:
                index = hash(node.key) % new_capacity
                if new_buckets[index]:
                    new_node = new_buckets[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                else:
                    new_buckets[index] = Node(node.key, node.value)
                node = node.next
        self.capacity = new_capacity
        self.buckets = new_buckets
#Рехэширование с помощью псевдослучайных чисел
class HashTableR:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size
    def randomFunction(self):
        return random.randint(0, self.size - 1)
    def put(self, key, data):
        index = key % self.size
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = data
        else:
            while self.keys[index] is not None:
                if self.keys[index] == key:
                    self.values[index] = data
                    return
                index = (index + self.randomFunction()) % self.size
            self.keys[index] = key
            self.values[index] = data
    def get(self, key):
        index = key % self.size
        if self.keys[index] is None:
            return None
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + self.randomFunction()) % self.size
        return None

bst = BinaryTree()
for num in [12,32,78,23,14,56]:
    bst.insert(num)
print(bst.printTree())

print("Исходный массив: ")
array = copy.deepcopy(generateMas())
find_elem = int(input("Введите элемент, который хотите найти: ", ))
print()

starttime = timeit.default_timer()
binary(array, find_elem)
endtime = timeit.default_timer()
print("Метод Бинарного поиска работал:", endtime - starttime, "секунд")

starttime = timeit.default_timer()
bst.search(find_elem)
endtime = timeit.default_timer()
print("Метод Бинарного дерева работал:", endtime - starttime, "секунд")

starttime = timeit.default_timer()
fibonachi_search(array, find_elem)
endtime = timeit.default_timer()
print("Метод Фиббоначиев поиск работал:", endtime - starttime, "секунд")

starttime = timeit.default_timer()
interpolation_search(array, find_elem)
endtime = timeit.default_timer()
print("Метод Интерполяционного поиска работал:", endtime - starttime, "секунд")

starttime = timeit.default_timer()
array.index(find_elem)
endtime = timeit.default_timer()
print("Метод поиска работал:", endtime - starttime, "секунд")

Table = HashTableP()

Table.put(1,"a")
Table.put(2, "b")
Table.put(11, "c")
Table.put(21, "d")

print(Table.get(1))
print(Table.get(2))
print(Table.get(11))
print(Table.get(21))

def is_safe(board, row, col):
    # Проверяем, не находится ли клетка под боем других ферзей
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row):
    size = len(board)
    if row == size:
        # Все ферзи успешно размещены
        return True

    for col in range(size):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1):
                return True
            board[row] = -1

    return False

def print_board(board):
    size = len(board)
    for row in range(size):
        line = ""
        for col in range(size):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

# Создаем доску размером 8x8
board = [-1] * 8

# Решаем задачу
if solve_n_queens(board, 0):
    print_board(board)
else:
    print("Решение не найдено")
