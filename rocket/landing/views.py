from django.shortcuts import render
from django.contrib.auth.hashers import make_password 
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def landing_page(request):
    return render(request, 'landing/landing.html')

def learn_more(request):
    return render(request, 'landing/learn_more.html')

def login(request):
    return render(request,'landing/register.html')


# Registration form

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # Check if the form input is valid
            user = form.save(commit=False)  # Create user object but don't save it yet
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user to the database after hashing the password
            return redirect('success_page')  # Redirect to a success page
    else:
        form = SignUpForm()  # If the request is not POST, render an empty form
    
    return render(request, 'landing/learn_more.html', {'form': form})  # Render the form in the template
