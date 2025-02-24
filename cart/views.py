from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .cart import Cart
from website.models import Product
from django.http import JsonResponse

def cart_summary(request):
    # Get a cart
    cart = Cart(request)

    # Get a products' quantities
    quantities = cart.get_quantities

    # Get cart products
    cart_products = cart.get_cart_products

    # Get totals
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})

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

        messages.success(request, "Product has been successfully added to your cart...")
        # Get a response 
        response = JsonResponse({'quantity': cart_quantity})
        return response
        
        # Get a response 
        #response = JsonResponse({'Product name': product.name})
        
        # Return a response 
        #return response

def cart_delete(request):
    # Get a cart
    cart = Cart(request)

    # If action is 'post'
    if request.POST.get('action') == 'post':

        # Get a product id
        product_id = int(request.POST.get('product_id'))

        cart.delete_product(product = product_id)

        response = JsonResponse({'product': product_id})
        messages.success(request, "Product has been successfully removed from your cart...")
        return response

def cart_update(request):
    # Get a cart
    cart = Cart(request)
    
    # If action is 'post'
    if request.POST.get('action') == 'post':

        # Get a product id
        product_id = int(request.POST.get('product_id'))

        # Get a product quantity 
        product_quantity = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_quantity)

        messages.success(request, "Quantity of the product has been successfully changed...")
        response = JsonResponse({'quantity': product_quantity})
        return response
