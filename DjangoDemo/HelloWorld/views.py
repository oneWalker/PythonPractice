from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context          = {}
    context['name'] = 'Hello World!'
    return render(request, 'runoob.html', context)