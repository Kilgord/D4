from django import template

register = template.Library()



# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.

@register.filter()
def censor(value):
    if isinstance(value, str):
        words = value.split()
        for word in words:
            if word == 'Редиска':
                value = value.replace("Редиска", "Р******")

    return f'{value}'



