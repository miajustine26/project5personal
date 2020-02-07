from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cart')
def home():
    return render_template('cart.html', cart=cart)

if __name__ == '__name__':
    app.run(debug=True)
