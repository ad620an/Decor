def fizz_buzz(start, finish):
    summa = 0
    for i in range (start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            summa = summa + i
        i = i + 1
    return summa


def html(tag_name, **kwargs):
    def html_decorator(func):
        def wrapper(input_value):
            part1 = f'<{tag_name}'
            part2 = ''
            part3 = f'{tag_name}'
            if len(kwargs.items()) == 0:
                part2 = ''
            else:   
                for k, v in kwargs.items():
                    part2 = f'{part2} {k}="{v}"'
            path = f'{part1}{part2}>{func(input_value)}</{part3}>'
            return path
        return wrapper
    return html_decorator


def plural_form(number,form1,form2,form3):
    correct_form = ''
    ultimate_digit = number % 10
    penultimate_digit = number % 100 - ultimate_digit  
    if penultimate_digit != 10:
        if ultimate_digit == 1:
            correct_form = form1
        else:
            if ultimate_digit < 5:
                correct_form = form2
            else:
                correct_form = form3    
    else:
        correct_form = form3
    return correct_form   


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))     


    
start = int(input('Введите целое число - начало диапазона: '))
finish = int(input('Введите целое число - конец диапазона: '))
string = f'{start}-{finish}:'
print(string, fizz_buzz(start,finish))   


print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))  


