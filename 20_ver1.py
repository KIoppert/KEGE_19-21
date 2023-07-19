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
    # Если какой-то ход ведет в проигрышную позицию для второго игрока,
    # то эта позиция выигрышная.
    if any(f(x) == 'LOSE1' for x in moves(summa)):
        return 'WIN2'
   
ans = []
for i in range(1, 81):
    if f(i + 20) == 'WIN2':  # i + 20,
        ans.append(i)  # так как изначально в числе есть 10 двоек.

print(ans[0], ans[-1])
