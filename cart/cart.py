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
    def add(self, product):

        # Get a product id
        product_id = str(product.id)

        # If product already in cart
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True