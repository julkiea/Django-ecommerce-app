from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .cart import Cart
from website.models import Product
from django.http import JsonResponse

def cart_summary(request):
    # Get a cart
    cart = Cart(request)

    # Get cart products
    cart_products = cart.get_cart_products
    return render(request, "cart_summary.html", {"cart_products": cart_products})

def cart_add(request):
    # Get a cart
    cart = Cart(request)
    
    # If action is 'post'
    if request.POST.get('action') == 'post':

        # Get a product id
        product_id = int(request.POST.get('product_id'))

        # Get a product quantity 
        product_quantity = int(request.POST.get('product_qty'))

        # Get a product 
        product = get_object_or_404(Product, id = product_id)
        
        # Save to a session
        cart.add(product = product, quantity = product_quantity)

        # Get cart quantity 
        cart_quantity = cart.__len__()

        # Get a response 
        response = JsonResponse({'quantity': cart_quantity})
        return response
        
        # Get a response 
        #response = JsonResponse({'Product name': product.name})
        
        # Return a response 
        #return response




def cart_delete(request):
    pass

def cart_update(request):
    pass