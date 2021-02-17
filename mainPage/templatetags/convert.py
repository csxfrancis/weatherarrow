from django import template

register = template.Library()

@register.filter(name='ktoF')
def ktoF(value):

    return "{:.2f}".format((value*(9/5) -459.67))
