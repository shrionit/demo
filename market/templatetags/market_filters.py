
from django.template import Library
  
register = Library()

@register.filter
def active_class(obj, args=None):
    if obj == 'Profile':
        return 'bg-stone-100'
    else:
        return 'bg-stone-200'

@register.filter
def fullname(obj, args=None):
    if obj is not None:
        return f'{obj.first_name} {obj.last_name}'


@register.filter
def check(obj, args):
    if obj is not None:
        return obj == args