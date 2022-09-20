from flask import render_template, redirect, flash
from app import create_app
from app.forms import SearchForm

app = create_app()

@app.route('/', methods=['GET'])
def main_page():
    form = SearchForm()
    context = {
        'form': form
    }
    if form.validate_on_submit():
        return redirect('/car_list')
    return render_template('index.html', **context)

@app.route('/car_list')
def carlist():
    
    return render_template('carlist.html')

if __name__ == '__main__':
    app.run(debug=True)