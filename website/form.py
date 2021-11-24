from django import forms
from .models import Contact

class newslatter(forms.Form):

   email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))

class contact(forms.ModelForm):
      class Meta:
         model=Contact
         fields ="__all__"
         widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control','name':'name','pattern':'[A-Za-z ]*','title':'Write a Your Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'abc@xyz.com', 'class': 'form-control','name':'email','pattern':'[A-Za-z0-9._%+-]+@[A-Za-z.]+\.[A-Za-z]{1,63}$','title':'Write a Orignal Email'}),
            'subjact': forms.TextInput(attrs={'placeholder': 'abc@xyz.com', 'class': 'form-control','name':'subjact','pattern':'[A-Za-z0-9- ]*','title':'Write a Subject'}),
            'message': forms.TextInput(attrs={'placeholder': 'abc@xyz.com', 'class': 'form-control','name':'message','title':'Write Your Message'}),
        }