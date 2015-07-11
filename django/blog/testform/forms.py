from django import forms

class MessageForm(forms.Form):
	author = forms.CharField(label="ОТ кого", max_length=8, error_messages={
	'required': 'You must enter name',
	 "max_length" : 'To much max_length'}
	 ) #by default required = True
	message = forms.CharField(label="Сообщение", widget = forms.Textarea)
	is_public = forms.BooleanField(label="Доступно всем")
	image = forms.FileField(label="Аватар")