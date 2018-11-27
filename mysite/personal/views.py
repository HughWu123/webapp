from django.shortcuts import render
from .forms import TestForm
from .models import To_Log

def index(request):
    return render(request, 'personal/home.html')

def login(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print(name, password)
            to_log = To_Log()
            To_Log.postsign(to_log, name, password)
            print('ce shi')
            To_Log.getLocation(to_log)
    form = TestForm()
    return render(request, 'personal/basic.html', {'form':form})

def register(request):
    return render(request, 'personal/basic2.html', {'content': ['Register Right Now!']})

def cancelbtn(request):
    return render(request, 'personal/home.html')