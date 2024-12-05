# Чтение строки чисел
numbers = input().split()

# Преобразуем строки в числа и вычисляем квадраты с использованием enumerate
for i, num in enumerate(numbers):
    numbers[i] = int(num) ** 2  # Преобразуем строку в число и возводим в квадрат

# Выводим список чисел через пробел
print(" ".join(map(str, numbers)))
