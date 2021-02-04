#-*- codeing = utf-8 -*-
#@Time : 2021/2/1  10:27
#@Aythor : LHW 
#@File : myfilter.py
#@Software: PyCharm

from django.template import Library

register = Library()

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)