from __future__ import division

from django import template
from django.template.defaultfilters import stringfilter

from BeautifulSoup import BeautifulSoup, Tag

from PIL import Image
from settings import MEDIA_ROOT, MEDIA_URL

register = template.Library()

@register.filter
def img_resize(value):
    """ Resize img for fitting with width """

    resized_width = 600

    soup = BeautifulSoup(value)
    imgs = soup.findAll('img')

    for img in imgs:
        im = Image.open(MEDIA_ROOT + img['src'][len(MEDIA_URL):])
        (width, height) = im.size
        if width > resized_width:
            ratio = width / resized_width
            tag = Tag(soup, "a", [('href', img['src'])])
            img['style'] = 'max-width:' + str(resized_width) + 'px;max-height:' + str(int(height / ratio)) + 'px'
            img_content = img
            img.replaceWith(tag)
            tag.insert(0, img_content)

    return soup
img_resize.is_safe = True
img_resize = stringfilter(img_resize)
