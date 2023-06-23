from django import template

register = template.Library()

@register.filter
def replace_url_param(value, replacement):
    return value.replace('?', replacement)