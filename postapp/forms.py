from django import forms
from postapp.models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'age']