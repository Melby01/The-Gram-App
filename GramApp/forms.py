from django import forms
from .models import Image,Profile,Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'Author', 'author_profile']
        

class GramLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    class Meta:
        model = Image
        exclude = ['pub_date', 'Author', 'author_profile']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 
        
        
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')   
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author']
