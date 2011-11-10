from django import template
from django.template.defaultfilters import stringfilter

from BeautifulSoup import BeautifulSoup

from pygments import highlight as hl
from pygments.lexers import PythonLexer, PythonConsoleLexer, BashSessionLexer, HtmlDjangoLexer
from pygments.formatters import HtmlFormatter

from xml.sax.saxutils import unescape

register = template.Library()

@register.filter
def highlight(value):
    """ Highlight the python code with pygments"""
    soup = BeautifulSoup(value)
    prespy = soup.findAll('pre', lang="python")
    prespyco = soup.findAll('pre', lang="python_console")
    presbs = soup.findAll('pre', lang="bash")
    presht = soup.findAll('pre', lang="html")

    for pre in prespy:
        pre.replaceWith(hl(unescape(pre.string), PythonLexer(), HtmlFormatter()))
    for pre in prespyco:
        pre.replaceWith(hl(unescape(pre.string), PythonConsoleLexer(), HtmlFormatter()))
    for pre in presbs:
        pre.replaceWith(hl(unescape(pre.string), BashSessionLexer(), HtmlFormatter()))
    for pre in presht:
        pre.replaceWith(hl(unescape(pre.string), HtmlDjangoLexer(), HtmlFormatter()))

    return soup
highlight.is_safe = True
highlight = stringfilter(highlight)
