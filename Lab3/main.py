import math
import networkx as nx
import matplotlib.pyplot as plt
import copy

def drawGraph(arr, mas):
    mr = [[0 for _ in range(2)] for _ in range(len(mas) - 1)]
    for i in range(len(mas) - 1):
        mr[i][0] = mas[i]
        mr[i][1] = mas[i + 1]

    from pyvis.network import Network
    g = Network(notebook=False, directed=True)
    g.add_nodes([1, 2, 3, 4, 5], value=[100, 100, 100, 100, 100],
                title=['1', '2', '3', '4', '5'],
                x=[21.4, 54.2, 11.2, 31.1, 45.1],
                y=[100.2, 23.54, 32.1, 45, 60],
                label=['1', '2', '3', '4', '5'],
                color=['#162347', '#162347', '#162347', '#162347', '#162347'])

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != 0 and arr[i][j] != math.inf:
                if [i + 1, j + 1] in mr:
                    g.add_edge(i + 1, j + 1, title=str(arr[i][j]), label=str(arr[i][j]), color='#ff0000')
                else:
                    g.add_edge(i + 1, j + 1, title=str(arr[i][j]), label=str(arr[i][j]))
    g.write_html('example.html')

def ford(arr, start, end):
    minPath = [math.inf] * len(arr)
    minPath[start-1] = 0
    for u in range(1, len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                minPath[j] = min(minPath[i] + arr[i][j], minPath[j])
    return minPath[end-1]

def djonson(arr, start, end):
    minPath = [0] * len(arr)
    for u in range(1, len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                minPath[j] = min(minPath[i] + arr[i][j], minPath[j])
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] =  arr[i][j] + minPath[i] - minPath[j]
    return deykstra(arr, start, end) - minPath[i] + minPath[j]


def levita(arr, start, end):
    m0 = []
    m11 = []
    m12 = []
    m2 = []
    current = start
    d = [math.inf] * len(arr)
    d[current] = 0
    m11.append(current)

    for i in range(len(arr)):
        if arr[current][i] != math.inf and i != current:
            m2.append(i)

    while len(m0) != len(arr):
        for i in range(len(arr)):
            if i not in m0 and arr[current][i] != math.inf:
                if i in m2:
                    d[i] = d[current] + arr[current][i]
                    m2.remove(i)
                    m11.append(i)
                elif i in m12:
                    d[i] = min(d[i], d[current] + arr[current][i])
                    m12.remove(i)
                    m0.append(i)
                elif i in m11:
                    d[i] = min(d[i], d[current] + arr[current][i])
                    m11.remove(i)
                    m0.append(i)
                elif i in m0:
                    if d[i] > d[current] + arr[current][i]:
                        d[i] = d[current] + arr[current][i]
                        m0.remove(i)
                        m11.append(i)

    if d[end] == math.inf:
        return "Путь не найден"
    else:
        return d[end]

def deykstra(arr, start, end):
    minPath = [math.inf] * len(arr)
    minPath[start-1] = 0
    visited = set()
    while len(visited) < len(arr):
        current = None
        for i in range(len(arr)):
            if i not in visited and (current is None or minPath[i] < minPath[current]):
                current = i
        visited.add(current)
        for i in range(len(arr)):
            if i not in visited and minPath[current] + arr[current][i] < minPath[i]:
                minPath[i] = minPath[current] + arr[current][i]

    return minPath[end-1]

def floyd(arr, start, end):
    n = len(arr)
    resMas = []
    mas = [0] * len(arr)
    for i in range(n):
        if(arr[start-1][i] != math.inf and arr[start-1][i] != 0):
            mas[i] = 1
    for u in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][u] + arr[u][j] < arr[i][j] :
                    arr[i][j] = arr[i][u] + arr[u][j]

                    if (arr[start - 1][j] >= arr[start - 1][i] + arr[i][j]):
                        mas[j] = u + 1

    a = end
    while a != start:
        resMas.insert(0, a)
        a = mas[a-1]
    resMas.insert(0, start)
    return resMas


file = open("Матрица смежности.txt")
arr = file.readlines()
for i in range(len(arr)):
    arr[i] = arr[i].strip().split(" ")
    for j in range(len(arr)):
        if(arr[i][j] == 'inf'):
            arr[i][j] = math.inf
        else:
            arr[i][j] = int(arr[i][j])


drawGraph(arr, floyd(copy.deepcopy(arr), 1, 5))
print(djonson(copy.deepcopy(arr), 1, 5))
print(deykstra(copy.deepcopy(arr),1, 5))
print(ford(copy.deepcopy(arr), 1, 5))