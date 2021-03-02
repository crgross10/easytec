
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def mysplit(v):
    vHtml = '<h6 class="white-text op-5 light-blue-text">'
    var = v.split('/')
    vRetorno=''

    cont = 0 # Lista somente 3 empresas para não ficar com a lista muito grande
    outras = 0 # conta a quantidade de unidade acima de 3

    for v in var:        
        cont = (cont + 1)
        if (cont < 5):
            vRetorno = vRetorno + vHtml + v + ' </h6> '
        else:
            outras = (outras + 1)

    if (outras > 0):
        vRetorno = vRetorno + vHtml + '+ ' + str(outras)

    return mark_safe(vRetorno)
