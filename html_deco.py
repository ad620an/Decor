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


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))