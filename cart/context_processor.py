from .cart import Cart


# Create context processor so cart can work on all pages
def cart(request):
    return {'cart': Cart(request)}