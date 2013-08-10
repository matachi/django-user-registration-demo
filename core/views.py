from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import UserSerializer

def index(request):
    request.breadcrumbs('Home', '')
    return render(request, 'core/index.html')

def about(request):
    context = {'current_page': 'about'}
    request.breadcrumbs((('Home', reverse('index')), ('About', '')))
    return render(request, 'core/about.html', context)

def help(request):
    context = {'current_page': 'help'}
    request.breadcrumbs((('Home', reverse('index')), ('Help', '')))
    return render(request, 'core/help.html', context)

class UsernameAvailable(APIView):
    def get(self, request, username, format=None):
        available = False
        try:
            User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            available = True
        serializer = UserSerializer({'available': available})
        return Response(serializer.data)
