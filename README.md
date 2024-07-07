# Django Book Shop

## Overview

The Django Book Shop is a web application designed to facilitate the sale and purchase of books. Built using Django, it includes features such as user authentication, browsing books, adding books to a shopping cart, placing orders, and processing payments through PayPal.

## Features

- User authentication and registration
- Browse books
- Add books to a shopping cart
- View and update cart items
- Place orders securely using PayPal for payment processing

## Installation

### Prerequisites

Ensure you have Python and pip installed on your system.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/munuhee/books_shop.git
   cd books_shop
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Django settings:**

   - Create a file named `.env`.
   - Update the `.env` file with your Django secret key and PayPal configurations:

     ```plaintext
     SECRET_KEY='your-django-secret-key'

     PAYPAL_CLIENT_ID='your-paypal-client-id'
     PAYPAL_SECRET='your-paypal-secret'

     EMAIL_HOST='smtp.example.com'
     EMAIL_PORT=587
     EMAIL_USE_TLS=True
     EMAIL_HOST_USER='your_email@example.com'
     EMAIL_HOST_PASSWORD='your_email_password'
     ```

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://localhost:8000`.

7. **Access the admin interface:**

   - Manage books and users via the Django admin interface at `http://localhost:8000/admin/`.

## Usage

1. **Sign up (registration):**

   - Users can register for an account to start purchasing books.

2. **Browse books:**

   - Browse through categories and lists of available books.

3. **Add to cart:**

   - Add desired books to the shopping cart for checkout.

4. **Checkout:**

   - Proceed to checkout, review cart items, and enter payment details.

## Contributing

We welcome contributions! To contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## Acknowledgments

- This project was created as part of learning Django and integrating PayPal for payment processing.
- Thanks to the Django and PayPal communities for their valuable documentation and resources.

Happy coding!
