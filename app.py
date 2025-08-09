from flask import Flask,render_template

app = Flask(__name__)

#about page route
@app.route("/about")
def about_page():
  return render_template('about_page.html')
#menu route with all item display functionality
@app.route("/menu")
def menu_page():
     items = [
        {'name': 'Espresso', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Latte', 'category': 'Coffee','img':'cappucino.png','price':'$5'},
        {'name': 'Green Tea', 'category': 'Tea','img':'cappucino.png','price':'$5'},
        {'name': 'Black Tea', 'category': 'Tea','img':'cappucino.png','price':'$5'},
        {'name': 'Croissant', 'category': 'Pastry','img':'cappucino.png','price':'$5'}
    ]

     from collections import defaultdict
     grouped_items = defaultdict(list)

     for item in items:
        grouped_items[item['category']].append(item)
     return render_template('menu_page.html', grouped_items=grouped_items)

#route for selected drink category
# @app.route("/filter/<category>")
# def filter(category):
    
    
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
@app.route('/feedback')
def feedback():
    return "<h2>Feedback page coming soon!</h2>"

# Run the development server
if __name__ == '__main__':
    app.run(debug=True) 