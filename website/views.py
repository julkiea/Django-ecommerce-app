from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'categories': categories})


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


def product(request, pk):
    try:
        product = get_object_or_404(Product, id=pk)
        return render(request, "product.html", {'product': product})
    except Product.DoesNotExist:
        messages.error(request, "Product does not exist...")
        return redirect('home')
    
    
"""
def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name= foo)
        products = Product.objects.filter(category = category)
        return render(request, "category.html", {'products': products, 'category': category})
    except:
        messages.error(request, "There is no product with this category...")
        return redirect('home')

"""
def filter_products(request):
        
    products = Product.objects.all()

    category_name = request.GET.get('category')
    categories = Category.objects.all()
    if category_name:
        products = products.filter(category__name=category_name)

    return render(request, 'home.html', {'products': products, 'categories': categories})

def update_user(request):
    return render(request, "update_user.html", {})