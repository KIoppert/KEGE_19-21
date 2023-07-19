from functools import cache

# Функция симулирующая ходы.
def moves(number):
    one, two = number
    return (one * 3, two * 3), (one + 2, two), (one + 1, two + 1)

# Обязательно прокешируем рекурсивную функцию для повышения скорости.
@cache
def f(number):
    one, two = number
    if one + two * 2 >= 101:
        return 'END'
    # Если какой-то ход дает победу, то текущая позиция выигрышная.
    if any(f(x) == 'END' for x in moves(number)):
        return 'WIN1'
    # Если все ходы ведут в выигрышную позицию для второго игрока,
    # то эта позиция проигрышная.
    if all(f(x) == 'WIN1' for x in moves(number)):
        return 'LOSE1'
    # Если какой-то ход ведет в проигрышную позицию для второго игрока,
    # то эта позиция выигрышная.
    if any(f(x) == 'LOSE1' for x in moves(number)):
        return 'WIN2'
    # Если все ходы ведут в выигрышную позицию для второго игрока,
    # то эта позиция проигрышная.
    if all(f(x) == 'WIN1' or f(x) == 'WIN2' for x in moves(number)):
        return 'LOSE2'

ans = []
for i in range(1, 81):
    if f((i, 10)) == 'LOSE2': # Аргумент - кортеж из кол-ва 1 и кол-ва 2.
        ans.append(i)

print(ans[-1], ans[-2])

