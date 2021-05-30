from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput


class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		fields = ['title', 'anons', 'date',]

		widgets = {
			"title": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Название'
			}),
			"anons": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Cумма'
			}),
			"date": DateTimeInput(attrs={
				'class': 'form-control',
				'placeholder': 'Дата'
			})
		}