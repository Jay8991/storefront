from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes in request and gives back response 

def say_hello(request):
    context = {"name": 'Jay'}
    return render(request, 'hello.html', context)
