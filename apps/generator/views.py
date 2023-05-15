import secrets
from django.shortcuts import render, redirect
from .models import Password
from .forms import PasswordGeneratorForm

def generate_password(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            uppercase = form.cleaned_data['uppercase']
            lowercase = form.cleaned_data['lowercase']
            numbers = form.cleaned_data['numbers']
            special_characters = form.cleaned_data['special_characters']
            characters = ''
            if uppercase:
                characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if lowercase:
                characters += 'abcdefghijklmnopqrstuvwxyz'
            if numbers:
                characters += '0123456789'
            if special_characters:
                characters += '!@#$%^&*()'
            password = ''.join(secrets.choice(characters) for _ in range(length))
            Password.objects.create(
                password_text=password,
                length=length,
                uppercase=uppercase,
                lowercase=lowercase,
                numbers=numbers,
                special_characters=special_characters
            )
            return redirect('passwords')
    else:
        form = PasswordGeneratorForm()
    
    return render(request, 'generate_password.html', {'form': form})

def password_list(request):
    passwords = Password.objects.all()
    return render(request, 'password_list.html', {'passwords': passwords})