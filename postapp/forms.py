from django import forms
from postapp.models import Profile, Comments

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'age']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ['comment']