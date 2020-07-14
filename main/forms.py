from django import forms

class ContactForm(forms.Form):
	Your_name = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "id":"name", "name":"name", "class":"form-control"}), required=True)
	Your_email = forms.EmailField(widget=forms.TextInput(attrs={"type":"text", "id":"email", "name":"email", "class":"form-control"}), required=True)
	subject = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "id":"subject", "name":"subject", "class":"form-control"}), required=True)
	message = forms.CharField(widget=forms.Textarea(attrs={"type":"text", "id":"message", "name":"message", "rows":"2", "class":"form-control md-textarea"}), required=True)
