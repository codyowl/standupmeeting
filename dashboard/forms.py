from django import forms

class RecipientForm(forms.Form):
	name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Receipt name'}))
	email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Receipt email'}))

class ComposeForm(forms.Form):
	emailbody = forms.CharField(required=True, widget=forms.Textarea())	