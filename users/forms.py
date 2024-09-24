from django.contrib.auth.forms import UserCreationForm

from content.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("phone_number", "password1", "password2")
