from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .cart import Cart
from website.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    # Get a cart
    cart = Cart(request)
    
    # If action is 'post'
    if request.POST.get('action') == 'post':

        # Get a product id
        product_id = int(request.POST.get('product_id'))

        # Get a product 
        product = get_object_or_404(Product, id = product_id)
        
        # Save to a session
        cart.add(product = product)
        
        # Get a response 
        response = JsonResponse({'Product name': product.name})
        
        # Return a response 
        return response




def cart_delete(request):
    pass

def cart_update(request):
    pass