
from django import template
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.utils.safestring import mark_safe
import json


register = template.Library()

@register.simple_tag
def alteracao(campo):
    dicCampos ={}
    dicCampos = json.loads(campo)
    vHtml = ''
    for k,v in dicCampos.items():
       if format(v[1]) == format(None):
           vHtml =  vHtml + '<b>'+ k + '</b>: ' + (v[0]) +  ';   '
       elif format(v[0]) == format(None):
           vHtml =  vHtml + '<b>'+ k + '</b>: ' + (v[1]) +  ';   '
       else:
           vHtml =  vHtml + '<b>'+ k + '</b> ' + '-  <u>Antes:</u> ' + (v[0]) + ' -  <u>Depois:</u> ' + (v[1]) + ';     '


    return mark_safe(vHtml)
