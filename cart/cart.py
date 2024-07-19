from website.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, there is no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make cart available on all pages
        self.cart = cart

    # Create add method
    def add(self, product, quantity):

        # Get a product id
        product_id = str(product.id)

        # Get a product quantity 
        product_quantity = str(quantity)

        # If product already in cart
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)

        self.session.modified = True

    # Get the quantity of products in cart
    def __len__(self):
        return len(self.cart)
    
    # Get the products from the cart
    def get_cart_products(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in =product_ids)
        return products
    
    # Get the products' quantities
    def get_quantities(self):
        quantities = self.cart
        return quantities
    
    # Update products' quantities
    def update(self, product, quantity):
        
        # Get a id 
        product_id = str(product)

        # Get a product's quantity 
        product_quantity = int(quantity)

        # Get a cart
        cart = self.cart

        # Update cart dictionary {'4': 1}; '4' - product id, 1 = product quantity
        cart[product_id] = product_quantity

        # Modify session 
        self.session.modified = True

        # Get updated cart
        updated_cart = self.cart
        return updated_cart
