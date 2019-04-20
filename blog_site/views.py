from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World, Welcome to django')

def lala(request):
    return HttpResponse('Lala')