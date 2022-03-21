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