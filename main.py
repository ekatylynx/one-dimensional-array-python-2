# Ввод данных
N = int(input("Введите количество элементов массива: "))
A = []

for i in range(N):
    A.append(int(input(f"Введите элемент {i+1}: ")))

B = int(input("Введите число B: "))

# Логика алгоритма
count = 0
product = 1
greater_numbers = []

for num in A:
    if num > B:
        count += 1
        product *= num
        greater_numbers.append(num)

# Вывод результатов
if count > 0:
    print(f"Числа, которые больше {B}: {greater_numbers}")
    print(f"Количество элементов: {count}")
    print(f"Произведение элементов: {product}")
else:
    print(f"В массиве нет чисел, которые больше {B}.")
