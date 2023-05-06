from django.contrib.auth.forms import UserCreationForm

from user_apps.company.models import Company

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
