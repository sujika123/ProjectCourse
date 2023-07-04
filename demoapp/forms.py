from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, userlogin, courses


class DateInput(forms.DateInput):
    input_type="date"

class Loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput,label = "password")
    password2 = forms.CharField(widget = forms.PasswordInput,label = "confirm password")
    class Meta:
        model = Login
        fields = ('username','password1','password2')

GENDER_CHOICES = (
    ('Male','male'),
    ('Female','Female'),
)

class userloginform(forms.ModelForm):
    gender = forms.ChoiceField(widget = forms.RadioSelect,choices = GENDER_CHOICES)
    class Meta:
        model = userlogin
        fields = ('name','gender','age','phone','address','image')

class courseaddform(forms.ModelForm):
    class Meta:
        model = courses
        fields = ('name', 'branches', 'duration', 'university', 'description')

