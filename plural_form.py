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


print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))  