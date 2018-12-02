from django import forms

class TestForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    CHOICES = [('User', 'User'),
               ('Location Employee', 'Location Employee'),
               ('Manager', 'Manager'),
               ('Admin', 'Admin')]
    #"User", "Location Employee", "Manager", "Admin"
    name = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password_again = forms.CharField(max_length=32, widget=forms.PasswordInput)
    email = forms.CharField()
    type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

class SearchForm(forms.Form):
    location_name = forms.CharField()
    CHOICES = [('Clothing', 'Clothing'),
               ('Hat', 'Hat'),
               ('Kitchen', 'Kitchen'),
               ('Electronics', 'Electronics'),
               ('Household', 'Household'),
               ('Other', 'Other')]
    category = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)