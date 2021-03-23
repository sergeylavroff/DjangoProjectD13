from django import template
import re

register = template.Library()

PATTERN_1 = [
        r'\w*ху[йие]\w*',
        r'\w*пизд\w*',
        r'\w*ебл\w*',
    # паттерны можно добавлять долго
    ]
@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        repl = ''
        for word in value.split():
            for pattern in PATTERN_1:
                if re.search(pattern, word.strip('.,;:?!-').lower()):
                    repl += '&%!%@' + ' '
                    break
            else:
                repl += word + ' '
        return str(repl)
    else:
        raise ValueError('Цензор обрабатывает только строки.')
