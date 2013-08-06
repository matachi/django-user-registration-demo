# coding=utf-8
from django import template
from django.utils.translation import ugettext as _

register = template.Library()

@register.filter
def page_title(title):
    base_title = _('Account Demo')
    return u'{} · {}'.format(title, base_title)
