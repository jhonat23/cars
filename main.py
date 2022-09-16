from flask import render_template
from app import create_app
from app.database import start_db

start_db()

app = create_app()

@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

