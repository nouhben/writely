from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from users.forms import UserSignupForm 
def register(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account was successfully registered for {username}! You can now login with using your details')
            return redirect('login')
        else:
            print(f'Registration failed: {form.errors}')
            messages.error(request, f'Account creation failed')

    else:
        form = UserSignupForm()
    
    return render(request, 'users/register.html', {'form': form})
from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    return render(request, 'users/profile.html')