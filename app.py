from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_func():
    # DB
    found = True

    if found:
        name = 'Arseni'
        return render_template('index.html', name=name, status=True)
    else:
        return render_template('index.html')



@app.route('/about')
def about_func():
    # DO SOMETHING WITH DB
    return render_template('about.html',
                           uni='BGU',
                           profile={'name': 'Arseni',
                                    'second_name': 'Perchik',
                                    'middle_name': 'Ariel'},
                           degrees=['BSc.', 'MSc.'],
                           hobbies=('art',
                                    'programming',
                                    'teaching',
                                    'horses',
                                    'travel',
                                    'music',
                                    'sql',
                                    'programming',
                                    'teaching',
                                    'horses',
                                    'travel',
                                    'music',
                                    'sql')
                           )


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


if __name__ == '__main__':
    app.run(debug=True)
