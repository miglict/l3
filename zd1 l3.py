# -*- coding: cp1251 -*-
from math import sqrt


# 1. Оформляем вычисление Y как отдельную функцию
def calculate_y(x):
    try:
        if x < -4:
            return -1
        elif -4 <= x < -2:
            return x + 3
        elif -2 <= x < 4:
            return -x / 2
        elif 4 <= x < 6:
            return -2
        elif 6 <= x < 10:
            # Проверка на отрицательное число под корнем (защита от ошибок float)
            val = 4 - (x - 8) ** 2
            if val < 0:
                return float('nan')
            return -2 + sqrt(val)
        else:  # x >= 10
            return -2
    except Exception as e:
        print(f"Ошибка вычисления при x={x}: {e}")
        return None


def main():
    print("Лабораторная работа №3. Задание 1. Вариант 5.")

    try:
        xb = float(input("Введите Xbeg: "))
        xe = float(input("Введите Xend: "))
        dx = float(input("Введите dx: "))

        if dx == 0:
            print("Ошибка: шаг не может быть равен 0")
            return

        with open("results.txt", "w", encoding="utf-8") as f:
            # 1. Заголовок параметров
            # Используем табуляцию \t или пробелы для отступа Dx
            header = f"Xbeg={xb:7.2f} Xend={xe:7.2f}\n\tDx={dx:7.2f}\n"

            # 2. Шапка таблицы с символом I
            # Обратите внимание: везде используются 'I' вместо '|'
            table_header = "+----------+----------+\nI    X     I    Y     I\n+----------+----------+\n"

            print(header, end="")
            print(table_header, end="")
            f.write(header)
            f.write(table_header)

            xt = xb
            while xt <= xe + 1e-9:
                y = calculate_y(xt)

                if y is not None:
                    # 3. Строка данных с символом I
                    # :^10 означает "выровнять по центру в поле шириной 10 символов"
                    line = f"I{xt:^10}I{y:^10}I\n"

                    print(line, end="")
                    f.write(line)

                xt += dx

            footer = "+----------+----------+\n"
            print(footer, end="")
            f.write(footer)

        print("\nРезультаты сохранены в results.txt")

    except ValueError:
        print("Ошибка ввода данных")


if __name__ == "__main__":
    main()