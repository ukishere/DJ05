from django.template import Library

register = Library()

@register.filter()
def order(value):
    return value.order_by('-tag')
