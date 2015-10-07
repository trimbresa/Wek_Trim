from django import forms

from .models import AddNewUser
from .models import AddResource

# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model  = AddNewUser
# 		fields = ['email', 'name', 'password']

class NameForm(forms.ModelForm):
	class Meta:
		model  = AddNewUser
		fields = ['email', 'name', 'password']

class NewResource(forms.ModelForm):
	class Meta:
		model  = AddResource
		fields = ['name', 'description', 'level', 'url']
		