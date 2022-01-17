"""
    Department classes to work with html forms
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class DepartmentForm(FlaskForm):
    """
        Form representing department creation form
    """
    name = StringField('Department name', validators=[DataRequired(), Length(min=0, max=50)])