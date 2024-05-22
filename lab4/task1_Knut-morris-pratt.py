# Алгоритм Кнута-Морриса-Пратта

import time

def compute_prefix_function(pattern):
    m = len(pattern)
    prefix = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        prefix[q] = k
    return prefix

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            print(f"Подстрока найдена на позиции {i - m + 1}")
            q = prefix[q - 1]

if __name__ == "__main__":
    text = input("Введите строку: ").strip()
    pattern = input("Введите подстроку: ").strip()
    case_sensitive = input("Чувствительность к регистру (y/n)? ").strip().lower() == "y"

    if not case_sensitive:
        text = text.lower()
        pattern = pattern.lower()

    start_time = time.time()
    kmp_search(text, pattern)
    elapsed_time = time.time() - start_time
    print(f"Время работы алгоритма КМП: {elapsed_time:.6f} секунд")

    start_time = time.time()
    occurrences = [i for i in range(len(text) - len(pattern) + 1) if text[i:i+len(pattern)] == pattern]
    elapsed_time = time.time() - start_time
    print(f"Время работы стандартной функции поиска: {elapsed_time:.6f} секунд")