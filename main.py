from flask import render_template, redirect, flash, url_for, make_response
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
        car_name = form.search_bar.data
        cars = get_cars(str(car_name))
        context_2 ={
            'cars': cars
        }
        
        return render_template('carfilter.html', **context_2)

    return render_template('index.html', **context)

@app.route('/car_list')
def carlist():
    cars = get_all_cars()
    context = {
        'cars': cars
    }
    return render_template('carlist.html', **context)

if __name__ == '__main__':
    app.run(debug=True)