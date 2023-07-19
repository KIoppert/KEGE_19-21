from functools import cache

# Функция симулирующая ходы.
def moves(summa):
    return (summa + 2, summa + 3, summa * 3)

# Обязательно прокешируем рекурсивную функцию для повышения скорости.
@cache
def f(summa):
    if summa >= 101:
        return 'END'
    # Если какой-то ход дает победу, то текущая позиция выигрышная.
    if any(f(x) == 'END' for x in moves(summa)):
        return 'WIN1'
    # Если все ходы ведут в выигрышную позицию для второго игрока,
    # то эта позиция проигрышная.
    if all(f(x) == 'WIN1' for x in moves(summa)):
        return 'LOSE1'

for i in range(1, 81):
    if f(i + 20) == 'LOSE1':  # i + 20,
        print(i)  # так как изначально в числе есть 10 двоек.
        break
