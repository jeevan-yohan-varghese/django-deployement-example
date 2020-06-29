from django import template


register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This filter cuts at value
    """
    return value.replace(arg,'')
