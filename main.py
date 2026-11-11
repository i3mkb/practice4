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

def main():
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

            # После смены размеров старый массив уже не подходит.
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
                print("Здесь появится меню пяти функций вашего варианта.")

        elif choice == "5":
            print("Программа завершена.")
            break

        else:
            print("Такого пункта нет. Попробуйте ещё раз.")


main()