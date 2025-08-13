from flask import Flask,render_template

app = Flask(__name__)

#about page route
@app.route("/about")
def about_page():
  return render_template('about_page.html')

@app.route('/contact')
def contact():
    return render_template('Contact_uspage.html')
@app.route('/cart')
def cart():
    # Example cart items
    cart_items = [
        {'id': 1, 'name': 'Cappuccino', 'image': 'cappuccino.png', 'quantity': 2, 'price': 4.50},
        {'id': 2, 'name': 'Sandwich', 'image': 'sandwich.png', 'quantity': 1, 'price': 6.00}
    ]
    subtotal = sum(item['price'] * item['quantity'] for item in cart_items)
    taxes = round(subtotal * 0.10, 2)  # Example 10% tax
    other_charges = 2.00  # Example other charges
    total = round(subtotal + taxes + other_charges, 2)
    return render_template(
        'Shopping_cart.html',
        cart_items=cart_items,
        subtotal=subtotal,
        taxes=taxes,
        other_charges=other_charges,
        total=total
    )
@app.route('/payment')
def payment():
    return render_template('payment.html')
@app.route('/feedback')
def feedback():
    return "<h2>Feedback page coming soon!</h2>"
@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

# Run the development server
if __name__ == '__main__':
    app.run(debug=True)