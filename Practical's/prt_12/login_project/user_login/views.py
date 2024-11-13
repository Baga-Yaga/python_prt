# user_login/views.py

from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'user_login/success.html')
    else:
        form = LoginForm()
    
    return render(request, 'user_login/login.html', {'form': form})
