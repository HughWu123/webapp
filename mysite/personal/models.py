#from django.db import models

#Create your models here.
#from django.db import models
import pyrebase
import requests
class To_Log:



    # Create your models here.
    config = {
        'apiKey': "AIzaSyCGHlTJLGrDjttALYY_yJxrRRlltBeoSEI",
        'project_id': "cs2340-donationtracker",
        'authDomain' : "cs2340-donationtracker.firebaseapp.com",
        'databaseURL' : "https://cs2340-donationtracker.firebaseio.com",
        'messagingSenderId' : "199547633680",
        "storageBucket": "cs2340-donationtracker.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    global authe
    authe = firebase.auth()
    database=firebase.database()

    def postsign(self, email, passw):
        #email = requests.POST.get('name')
        #passw = requests.POST.get("password")
        try:
            x = authe.sign_in_with_email_and_password(email, passw)
            print(x)
            if not 'localId' in x:
                return False
            return x
        except Exception as e:
            message = "invalid credentials"
            print(e)
            return False

        #use uid to query in database. store uid in some place




    global url
    url = "http://162.243.172.39:8080" # api url
    '''
    api available
        http.HandleFunc("/verify", verify_handler(db))
        http.HandleFunc("/register", create_user(db))
        http.HandleFunc("/getLocation", get_locations(db))
        http.HandleFunc("/userType", get_user_type(db))
        http.HandleFunc("/addItem", add_item(db))
        http.HandleFunc("/editLocation", add_location(db))
        http.HandleFunc("/searchItemByCategory", searchByCategory(db))
        http.HandleFunc("/searchItemByCategoryLoc", searchByCategory_loc(db))
        http.HandleFunc("/searchItemByName", searchByName(db))
        http.HandleFunc("/searchItemByNameLoc", searchByName_loc(db))
        http.HandleFunc("/getItems", get_items(db))
    '''
    # example 1
    def getLocation(self):
        r = requests.post(url+'/getLocation', data = {})
        print(type(r.json()))
        print(r.json())
        return r.json()

    def getLocationName(self, location_data):
        name = []
        for entry in location_data:
            name.append(entry.get('name'))
        return name

    def getLocationAddress(self, location_data):
        addr = []
        for entry in location_data:
            dictionary = {'lat': float(entry.get('latitude')), 'lng': float(entry.get('longitude'))}
            addr.append(dictionary)
        return addr

    def getAllInfo(self, location_data, locName):
        temp = []
        result = []
        for entry in location_data:
            if entry.get('name') == locName:
                temp = entry.items()
                for k, v in temp:
                    result.append(k + ': ' + v)
        return result

    # user is user email (e.g. 1@1.com) pw is the uid after user pass the authentication
    # uid for 1@1.com is NfTPhqOgdsbb5qaq27aEkvY6kqf1
    def addItems(self, user, pw, name, location, timestamp, f, v, cat):
        r = requests.post(url+'/addItems', data = {'username': user, 'pw': pw,
            'name': name, 'location': location, 'timestamp': timestamp, 'fulldescription': f,
            'value': v, 'category': cat})
        print(r) # if 1 then added successfully
    #



    def getItems(self, user, pw, location):
        r = requests.post(url+'/getItems', data = {'username': user, 'pw': pw,
            'location': location})
        print(r.json) # should be a json. a test location input can be AFD Station 4

    def searchItemsByCategory(self, user, pw, category):
        r = requests.post(url+"/searchItemByCategory", data = {'username': user, 'pw': pw, 'category': category})
        print(r.json())

    def searchItemsByCategoryLoc(selfs, user, pw, category, location):
        r = requests.post(url + "/searchItemByCategoryLoc", data={'username': user, 'pw': pw, 'category': category, 'location':location})
        print(r.json())

    def searchItemsByName(self, user, pw, name):
        r = requests.post(url + "/searchItemByName",data={'username': user, 'pw': pw, 'name': name})
        print(r.json())

    def searchItemsByNameLoc(self, user, pw, name, location):
        r = requests.post(url + "/searchItemByNameLoc", data={'username': user, 'pw': pw, 'name': name, 'location':location})
        print(r.json())

    def createNewUserInDB(self, user, uid, email, type):
        r = requests.post(url + "/register", data={'user': user, 'pw': uid, 'email': email, 'user_type': type})
        return r.json()

    def createNewUser(self, user, pw):
        res = authe.create_user_with_email_and_password(user,pw)
        return res
