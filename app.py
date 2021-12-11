from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home():
    # DO SOMETHING WITH DB
    return render_template('home_page.html')



@app.route('/about')
def about_func():
    # DO SOMETHING WITH DB
    return render_template('about.html')


@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/catalog')
def catalog_func():
    return render_template('catalog.html', color='green')

@app.route('/navigation_map')
def navigation_map():
    return render_template('navigation_map.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')



@app.route('/registeration')
def registeration():
    return render_template('registeration.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')




if __name__ == '__main__':
    app.run(debug=True)
