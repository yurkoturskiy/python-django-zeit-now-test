from django.http import HttpResponse
from django import get_version

source = 'https://github.com/zeit/now-examples/tree/master/python-django'
css = '<link rel="stylesheet" href="/css/style.css" />'

def index(request):
    return HttpResponse("%s<h1>Django on Now 2.0</h1><p>You are viewing a Django application written in Python running on Now 2.0.</p><p>Visit the <a href='./about'>about</a> page or view the <a href='%s'>source code</a>.</p>" % (css, source), content_type='text/html')

def about(request):
    return HttpResponse("%s<h1>ABOUT</h1><ul><li>WSGI Enabled</li><li>Django version <em>%s</em></li></ul><p>Visit the <a href='./'>home</a> page.</p>" % (css, get_version()), content_type='text/html')
