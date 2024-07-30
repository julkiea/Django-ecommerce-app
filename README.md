# Django E-commerce Application 🛒
This project is an e-commerce platform built with Django & Python. Please note that this application is currently under development and not all features are implemented yet.

## Features ✨
- Product listing
- About us section
- User registration and login
- Product's details
- Category pages
- Adding products to cart and update quantity of product in cart
- Deleting products from cart
- Counting cart total
- Updating user profile
- Updating user password
- Searching products

## Installation 🔧

1. Clone the repository:
   
    ```bash
    git clone https://github.com/julkiea/Django-ecommerce-app.git
    cd Django-ecommerceapp
    ```

2. Install `virtualenv`:
    ```bash
    pip install virtualenv
    ```

3. Create a new virtual environment:
    ```bash
    virtualenv virt
    ```

4. Activate the virtual environment:
    ```bash
    source virt/Scripts/activate
    ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Create a `.env` file in the project root directory and set your environment variables:
     ```bash
    # Example .env file
    SECRET_KEY=my_secret_key_value
    DEBUG=True
    ```
     
8. Generate a new secret key. You can use the following Python script to generate one:

   ```python
   import secrets
   print(secrets.token_urlsafe(50))


9. Apply migrations:
    ```bash
    python manage.py migrate
    ```

10. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

11. Run the development server:
    ```bash
    python manage.py runserver
    ```
