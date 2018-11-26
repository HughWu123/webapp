from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def login(request):
    return render(request, 'personal/basic.html', {'content':['Login Right Now!']})

def register(request):
    return render(request, 'personal/basic2.html', {'content': ['Register Right Now!']})

def cancelbtn(request):
    return render(request, 'personal/home.html')