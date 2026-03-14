from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


### for creating form with the help of Django
class RegistrationForm(UserCreationForm):
    class meta:
        model=User
        fields=('username','password1', 'password2')


