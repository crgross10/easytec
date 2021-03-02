
from django import template
from time import gmtime, strftime
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def data_atual():
    data = strftime("%d/%m/%Y - %H:%M:%S", gmtime())
    #vHtml= '<h1 style="font-size:10px;">'+format(data)+'</h1>'
    return data
