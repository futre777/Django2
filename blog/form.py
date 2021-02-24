from django import forms  
from blog.models import BlogMessage 

class MessageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs.update({'class':'form-control', 'id':'subject'})
		self.fields['email'].widget.attrs.update({'type': 'email', 'class':'form-control', 'id':'email'})
		self.fields['mensagem'].widget.attrs.update({'id':'message','cols':'30', 'rows':'7', 'class':'form-control', 'placeholder':'Escreve teus notes ou perguntas aqui...'})

	class Meta:
		model = BlogMessage
		fields = ['nome', 'email', 'mensagem'] 

