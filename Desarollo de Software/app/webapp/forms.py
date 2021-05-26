from django import forms
from django.forms import ModelForm

from .models import *

class ThreadForm(forms.ModelForm):
	class Meta:
		model = Thread
		fields = '__all__'
		widgets = {
			'username':forms.TextInput(
				attrs = {'class':'form-control'}
				),
			'text':forms.Textarea(
				attrs = {'class':'form-control'}
				),
			

			
			'title':forms.TextInput(
				attrs = {'class':'form-control'}
				),
			
		}

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = {
			'username',
			'text'
		}
		widgets = {
			'text':forms.Textarea(
				attrs = {'class':'form-control'}
				),

			'username':forms.TextInput(
				attrs = {'class':'form-control'}
				),
			
		}