'''Практическая работа 4 работа с матрицами'''
import random

def read_positive_number(message):
    """Просит ввести целое положительное число."""
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number

            print("Число должно быть больше нуля.")

        except ValueError:
            print("Нужно ввести целое число.")

def create_array(rows, columns):
    """Создаёт массив вручную или заполняет случайными числами."""

    while True:
        print("\nСоздание массива:")
        print("1. Ввести элементы вручную")
        print("2. Заполнить случайными числами")
        print("3. Назад")

        choice = input("Выберите пункт: ")

        if choice == "1":
            matrix = []

            for i in range(rows):
                row = []

                for j in range(columns):
                    while True:
                        try:
                            value = int(input(f"Введите элемент [{i}][{j}]: "))
                            row.append(value)
                            break
                        except ValueError:
                            print("Нужно ввести целое число.")

                matrix.append(row)

            return matrix

        elif choice == "2":
            matrix = []

            for i in range(rows):
                row = []

                for j in range(columns):
                    row.append(random.randint(0, 100))

                matrix.append(row)

            return matrix

        elif choice == "3":
            return None

        else:
            print("Такого пункта нет. Попробуйте ещё раз.")

def show_array(matrix):
    """Печатает массив построчно."""
    if matrix is None:
        print("Сначала создайте массив.")
        return

    for row in matrix:
        print(row)


def row_and_column_sums(matrix):
    """Функция № 6: суммы строк и столбцов"""

    for i, row in enumerate(matrix, start=1):
        print(f"Сумма строки {i}: {sum(row)}")

    for j, col in enumerate(zip(*matrix), start=1):
        print(f"Сумма столбца {j}: {sum(col)}")


def rows_with_ten(matrix):
    '''	Функция № 16: строки с числом 10'''

    found = False

    for i, row in enumerate(matrix, start=1):
        if 10 in row:
            print(f"В строке {i} есть число 10")
            found = True


    if not found:
        print("Числа 10 в массиве нет.")

def column_with_largest_sum(matrix):
    '''	Функция № 21: столбец с наибольшей суммой'''

    columns = len(matrix[0])
    sums = []

    for j in range(columns):
        total = 0

        for i in range(len(matrix)):
            total += matrix[i][j]

        sums.append(total)

    largest_sum = max(sums)

    print(f"Наибольшая сумма: {largest_sum}")

    for j in range(columns):
        if sums[j] == largest_sum:
            print(f"Это столбец {j + 1}")


def main_diagonal_sum(matrix):
    '''Функция № 23: сумма главной диагонали'''

    total = 0

    diagonal_size = min(len(matrix), len(matrix[0]))

    for i in range(diagonal_size):
        total += matrix[i][i]

    print(f"Сумма главной диагонали: {total}")


def replace_below_first_row_sum(matrix):
    '''Функция № 29: замена элементов'''

    first_row_sum = sum(matrix[0])
    print(f"Сумма первой строки: {first_row_sum}")

    for row in matrix:
        for j, val in enumerate(row):
            if val < first_row_sum:
                row[j] = first_row_sum


    print("Массив после замены:")
    show_array(matrix)


def run_functions(matrix):
    '''Меню выполнения функций'''

    while True:
        print("\n=== Функции варианта 5 ===")
        print("1. Суммы строк и столбцов")
        print("2. Найти строки, содержащие число 10")
        print("3. Найти столбец с наибольшей суммой")
        print("4. Найти сумму главной диагонали")
        print("5. Заменить числа меньше суммы первой строки")
        print("6. Назад")

        choice = input("Выберите функцию: ")

        if choice == "1":
            row_and_column_sums(matrix)
        elif choice == "2":
            rows_with_ten(matrix)
        elif choice == "3":
            column_with_largest_sum(matrix)
        elif choice == "4":
            main_diagonal_sum(matrix)
        elif choice == "5":
            replace_below_first_row_sum(matrix)
        elif choice == "6":
            break
        else:
            print("Такого пункта нет.")

def main():
    '''Основное меню'''

    rows = None
    columns = None
    matrix = None

    while True:
        print("\n=== Главное меню ===")
        print("1. Ввести размер массива")
        print("2. Создать массив")
        print("3. Показать массив")
        print("4. Выполнить функцию")
        print("5. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            rows = read_positive_number("Введите количество строк: ")
            columns = read_positive_number("Введите количество столбцов: ")

            matrix = None

        elif choice == "2":
            if rows is None or columns is None:
                print("Сначала задайте размеры массива.")
            else:
                new_matrix = create_array(rows, columns)

                if new_matrix is not None:
                    matrix = new_matrix

        elif choice == "3":
            show_array(matrix)

        elif choice == "4":
            if matrix is None:
                print("Сначала создайте массив.")
            else:
                run_functions(matrix)

        elif choice == "5":
            print("Программа завершена.")
            break

        else:
            print("Такого пункта нет. Попробуйте ещё раз.")


main()
