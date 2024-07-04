# Django eBook Shop

## Overview

The Django eBook Shop is a web application built using Django, designed to facilitate the sale and purchase of eBooks. It includes features such as user authentication, browsing eBooks, adding them to a shopping cart, placing orders, and processing payments through Stripe.

## Features

- User authentication and registration
- Browse eBooks by category
- Add eBooks to a shopping cart
- View and update cart items
- Place orders securely using Stripe for payment processing
- View order history and details
- Responsive design for mobile and desktop

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd django-ebook-shop
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Django settings:**

   - Rename `example.env` to `.env`.
   - Update `.env` with your Django secret key and Stripe API keys:

     ```plaintext
     DEBUG=True
     SECRET_KEY=your_django_secret_key
     STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
     STRIPE_SECRET_KEY=your_stripe_secret_key
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

   - Create and manage eBooks and users via the Django admin interface at `http://localhost:8000/admin/`.

## Usage

1. **Sign up (registration):**

   - Users can register for an account to start purchasing eBooks.

2. **Browse eBooks:**

   - Browse through categories and lists of available eBooks.

3. **Add to cart:**

   - Add desired eBooks to the shopping cart for checkout.

4. **Checkout:**

   - Proceed to checkout, review cart items, and enter payment details.

5. **View orders:**

   - Users can view their order history and details of past purchases.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- This project was created as part of learning Django and integrating Stripe for payment processing.
- Thanks to the Django and Stripe communities for their valuable documentation and resources.
