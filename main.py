from flask import render_template, redirect, flash, url_for, make_response, request
from app import create_app
from app.forms import SearchForm
from app.database import get_all_cars, get_cars

app = create_app()

@app.route('/')
def root():
    response = make_response(redirect('/home'))
    return response

@app.route('/home', methods=['GET', 'POST'])
def main_page():
    form = SearchForm()
    context = {
        'form': form
    }
    if form.validate_on_submit():
        return redirect(url_for('search'))

    return render_template('index.html', **context)

@app.route('/search', methods=['GET', 'POST'])
def search_cars():    
    form = SearchForm()
    car = form.search_bar.data
    cars = get_cars(car)
    context = {
        'form': form,
        'cars': cars
    }
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('carfilter', query=car))
    return render_template('carfilter.html', **context)

@app.route('/car_list')
def carlist():
    form = SearchForm()
    cars = get_all_cars()
    context = {
        'cars': cars,
        'form': form
    }
    return render_template('carlist.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)