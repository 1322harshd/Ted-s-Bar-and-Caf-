from flask import Flask,render_template

app = Flask(__name__)

#about page route
@app.route("/about")
def about_page():
  return render_template('about_page.html')

# Run the development server
if __name__ == '__main__':
    app.run(debug=True) 