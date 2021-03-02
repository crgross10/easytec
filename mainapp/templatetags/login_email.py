
from django import template
from django.utils.safestring import mark_safe

register = template.Library()
from django.core.mail import send_mail

@register.simple_tag
def enviaEmail():
    send_mail(
        'Subject here',
        'Here is the message.',
        'cristianogross@hushmail.com',
        ['cristianogross@outlook.com'],
        fail_silently=False,
    )

    return True
