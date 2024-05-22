import random
import time
import copy
import heapq

m = int(input())
n = int(input())
min = int(input())
max = int(input())

print("Hello World!")

# Создание рандомной матрицы
def randomArr(n, m, min, max):
    arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = random.randint(min, max)
    return arr


# Стандартная соортировка
start_time = time.time()
array = randomArr(n, m, min, max)
for i in range(n):
    array[i] = array[i].sort()
print("sortStandart"
      "--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# Соортировка выбором
start_time = time.time()
array = randomArr(n, m, min, max)
def sortVibor(arr, n, m):
    for i in range(n):
        for u in range(m):
            min_index = u
            for j in range(u, m):
                if arr[i][j] < arr[i][min_index]:
                    min_index = j
            arr[i][u], arr[i][min_index] = arr[i][min_index], arr[i][u]
    return arr
arr = sortVibor(copy.deepcopy(array), n, m)
print("sortVibor"
      "--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# Соортировка вставкой
start_time = time.time()
arr = randomArr(n, m, min, max)
def sortVstavka(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
for i in range(n):
    arr[i] = sortVstavka(arr[i])
print("sortVstavka"
      "--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# Турнирная сортировка
start_time = time.time()
arr = randomArr(n, m, min, max)
def tournament_sort(array):
    MAX_SIZE = len(array)
    size = len(array)
    pq = []
    for _ in range(MAX_SIZE):
        heapq.heappush(pq, array.pop(0))
    winners = []
    losers = []

    while array:
        if not winners:
            winners.append(pq[0])
            heapq.heappop(pq)

        if array[0] > winners[-1]:
            heapq.heappush(pq, array.pop(0))
        else:
            losers.append(array.pop(0))

        if pq:
            winners.append(pq[0])
            heapq.heappop(pq)

    while pq:
        winners.append(pq[0])
        heapq.heappop(pq)

    if not losers:
        return winners

    array = losers + winners
    while len(array) > size:
        array.pop()

    return tournament_sort(array)

for i in range(n):
    arr[i] = tournament_sort(arr[i])

print("sortTurnir"
      "--- {0} ms ---".format(round((time.time() - start_time)*1000)))


# Сортировка Шелла
start_time = time.time()
arr = randomArr(n, m, min, max)
def sortShell(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Пример использования функции
for i in range(n):
    arr[i] = sortShell(arr[i])

print("sortShell"
      "--- {0} ms ---".format(round((time.time() - start_time) * 1000)))


# Быстрая сортировка
start_time = time.time()
arr = randomArr(n, m, min, max)
def sortBistro(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return sortBistro(less) + [pivot] + sortBistro(greater)

# Пример использования функции
for i in range(n):
    arr[i] = sortBistro(arr[i])
print(arr)
print("sortBistro"
      "--- {0} ms ---".format(round((time.time() - start_time) * 1000)))


# Сортировка пузырьком
start_time = time.time()
arr = randomArr(n, m, min, max)
def sortPuzirkom(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Пример использования функции
for i in range(n):
    arr[i] = sortPuzirkom(arr[i])
print(arr)
print("sortPuzirkom"
      "--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
