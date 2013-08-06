from django.core.urlresolvers import reverse
from django.shortcuts import render

def index(request):
    request.breadcrumbs('Home', '')
    return render(request, 'core/index.html')

def about(request):
    context = {'page': 'about'}
    request.breadcrumbs((('Home', reverse('index')), ('About', '')))
    return render(request, 'core/help.html', context)

def help(request):
    context = {'page': 'help'}
    request.breadcrumbs((('Home', reverse('index')), ('Help', '')))
    return render(request, 'core/help.html', context)
