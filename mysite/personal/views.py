from django.shortcuts import render
from .forms import TestForm
from .forms import SearchForm
from .models import To_Log
from .forms import RegisterForm
from django import forms as f

to_log = To_Log()
global location_data
location_data = To_Log.getLocation(to_log)
location_name = To_Log.getLocationName(to_log, location_data)
cat_glob = None
usr = None
passw = None
def index(request):
    return render(request, 'personal/home.html')

def login(request):
    result = False
    name = ''
    print('method:' + request.method)
    if request.method == 'POST':
        form = TestForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            global usr
            usr = str(name)
            to_log = To_Log()
            result = To_Log.postsign(to_log, name, password)
            #if result is not None:
                #passw = result.get('localId')
            #rint(passw)
            To_Log.getLocation(to_log)
    form = TestForm()
    if result == False:
        return render(request, 'personal/basic.html', {'form': form, 'result': result})
    else:
        global passw
        passw = result.get('localId')
        #return render(request, 'personal/locations.html', {'form': form, 'username': name, 'pw': result['localId'] if 'localId' in result else ''})
        return showLoc(request)


def register(request):
    #message = 'Enter valid information'
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
                    message = str(e);
                    print(str(e))
            else:
                message = "two password do not match"
            #print(type(res))
            #uid = res[0].get('localId')
            #print(uid)
    #print(message)
    else:
        message = "Hello check valid info"

    form = RegisterForm()
    return render(request, 'personal/reg.html', {'form':form, 'm':message})

def showLoc(request):
    to_log = To_Log()
    cat = "check ////"
    print(cat)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        print(form)
        print('111111111111111')
        if form.is_valid():
            name = form.cleaned_data['location_name']
            cat = form.cleaned_data['category']
            print(cat + '////////////////////////////////////////')
            print(name, cat)
            return items(request)

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
    addr = To_Log.getLocationAddress(to_log, location_data)
    print(addr)
    return render(request, 'personal/map.html', {'addr': addr})

def items(request):
    print(usr,passw,cat_glob)
    ret_val = To_Log.searchItemsByCategory(to_log, usr, passw, cat_glob)
    print('ce shi')
    return render(request, 'personal/items.html', {'ret_val': ret_val})