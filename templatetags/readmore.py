from django import template
from django.template.defaultfilters import stringfilter
from django.utils.translation import ugettext as _

register = template.Library()

@register.filter
def readmore(value, arg):
    """ Add a Readmore link to the content"""
    from django.utils.text import truncate_html_words
    length = 100
    readmore = _('Read more')
    end_text = '...<a href="' + arg + '" style="font-size: 75%;">' + readmore + '</a>'
    return truncate_html_words(value, length, end_text)
readmore.is_safe = True
readmore = stringfilter(readmore)

