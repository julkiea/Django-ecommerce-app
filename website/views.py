from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about_us(request):
    return render(request, 'about_us.html')

def login_user(request):
    # Checking if logging in 
    if request.method == "POST":

        # Getting username and password
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticating user
        user = authenticate(request, username = username, password = password)

        # Checking if authenticating is success 
        if user is not None:
            
            # Logging in 
            login(request, user)

            # Displaying message 
            messages.success(request, "You have been logged in successfully!")

            # Redirect home
            return redirect('home')
        
        # If not success
        else: 

            # Displaying message
            messages.success(request, "An error occurred while logging in, please try again!")
            
            # Redirect home
            return redirect('home')

    return render(request, "login_user.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('home')

def register_user(request):
    # Check if signing in
    if request.method == 'POST':

        # Create instance of SignUpForm
        form = SignUpForm(request.POST)

        # Check if form is valid
        if form.is_valid():

            # Create a user 
            form.save()
            
            # Get username and password from cleaned data from form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None:

                login(request, user)

                # If authentication is successful
                messages.success(request, "You have been signed up successfully")

                # Redirect home
                return redirect('home')
            
            else:
                messages.success(request, "Authentication failed. Please try again.")
 
    else:
        form = SignUpForm()
        return render(request, 'register_user.html', {'form':form})

    return render(request, 'register_user.html', {'form': form})