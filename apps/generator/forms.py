from django import forms

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(label='Longitud de la contraseña')
    uppercase = forms.BooleanField(required=False, label='Incluir letras mayúsculas')
    lowercase = forms.BooleanField(required=False, label='Incluir letras minúsculas')
    numbers = forms.BooleanField(required=False, label='Incluir números')
    special_characters = forms.BooleanField(required=False, label='Incluir caracteres especiales')