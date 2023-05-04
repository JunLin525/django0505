#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import CustomUser
from django import forms
from .models import Comment
'''
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields'''

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ("comments", "author")