from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_bar = StringField('search_bar', validators=[DataRequired()])
    go = SubmitField()