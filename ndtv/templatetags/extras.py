# Django
from django import template

register = template.Library()


@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None


@register.filter
def return_item_list(l):
    try:
        return l.entries
    except:
        return None
