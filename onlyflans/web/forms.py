# forms.py
from django import forms
from .models import ContactForm
from django.contrib.auth.models import User


#form de registro.. no tiene models porque se uso en views.py def registro "user = User.objects.create_user(username, email, password)"
class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#contact form con atributos ya establecidos
class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        
        
#contact form con atributos personalizados
class ContactFormForm(forms.Form):
    #contact_form_uuid No necesita ser declarado en nuestro form
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')
