from django.shortcuts import render
from .forms import TestForm
from .forms import SearchForm
from .models import To_Log
from .forms import RegisterForm

to_log = To_Log()
global location_data
location_data = To_Log.getLocation(to_log)
location_name = To_Log.getLocationName(to_log, location_data)



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
    message = 'Enter valid information'
    confirmed = False
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            email = form.cleaned_data['email']
            type = form.cleaned_data['type']
            if password_again == password:
                confirmed = True
            print('good')
            to_log = To_Log()
            if confirmed:
                try:
                    res = To_Log.createNewUser(to_log, email, password)
                    #print(res)
                    uid = res.get('localId')
                    suc = To_Log.createNewUserInDB(to_log, name, uid, email, type)
                    print(suc)
                    if str(suc) == '1':
                        message = "user registration successful"
                    else:
                        message = "user registration not successful"
                except Exception as e:
                    message = 'Enter valid information'
                    print(str(e))
            else:
                message = "two password don't match"
            #print(type(res))
            #uid = res[0].get('localId')
            #print(uid)
    print(message)

    form = RegisterForm()
    return render(request, 'personal/basic2.html', {'form':form, 'm':message})

def showLoc(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(name, cat)

            print('ce shi')
    form = SearchForm()
    return render(request, 'personal/locations.html', {'form':form})

def afd(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(name, cat)

            print('ce shi')
    form = SearchForm()
    return render(request, 'personal/afd.html', {'content': To_Log.getAllInfo(to_log, location_data, 'AFD Station 4'), 'form' : form})

def b(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(name, cat)

            print('ce shi')
    form = SearchForm()
    return render(request, 'personal/b.html', {'content': To_Log.getAllInfo(to_log, location_data, 'BOYS & GILRS CLUB W.W. WOOLFOLK'), 'form' : form})

def pathway(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(name, cat)

            print('ce shi')
    form = SearchForm()
    return render(request, 'personal/pathway.html', {'content': To_Log.getAllInfo(to_log, location_data, 'PATHWAY UPPER ROOM CHRISTIAN MINISTRIES'), 'form' : form})

def pavilion(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(name, cat)

            print('ce shi')
    form = SearchForm()
    return render(request, 'personal/pavilion.html', {'content': To_Log.getAllInfo(to_log, location_data, 'PAVILION OF HOPE INC'), 'form' : form})

def dd(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(name, cat)

            print('ce shi')
    form = SearchForm()
    return render(request, 'personal/dd.html', {'content': To_Log.getAllInfo(to_log, location_data, 'D&D CONVENIENCE STORE'), 'form' : form})

def keep(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(name, cat)

            print('ce shi')
    form = SearchForm()
    return render(request, 'personal/keep.html', {'content': To_Log.getAllInfo(to_log, location_data, 'KEEP NORTH FULTON BEAUTIFUL'), 'form' : form})

def map(request):
    return render(request, 'personal/map.html')