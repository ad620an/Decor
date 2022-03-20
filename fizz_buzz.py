def fizz_buzz(start, finish):
    summa = 0
    for i in range (start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            summa = summa + i
        i = i + 1
    return summa


start = int(input('Введите целое число - начало диапазона: '))
finish = int(input('Введите целое число - конец диапазона: '))
string = f'{start}-{finish}:'
print(string, fizz_buzz(start,finish))   