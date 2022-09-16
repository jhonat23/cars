from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from app.config import Config


app = Flask(__name__)

#load config
app.config.from_object(Config)

# add bootstrap framework
bootstrap = Bootstrap(app)

#Create an object to use SQLalchemy features
db = SQLAlchemy(app)

@app.route('/')
def main_page():
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)