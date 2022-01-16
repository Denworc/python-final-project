"""

"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired
# from markupsafe import Markup


class EmployeeForm(FlaskForm):
    """

    """
    name = StringField('Name', validators=[DataRequired(), Length(min=0, max=50)])
    department_id = SelectField('Department', coerce=int, validators=[DataRequired()])

    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[InputRequired(), NumberRange(min=0)])


class EmployeeSearchForm(FlaskForm):
    """

    """
    start_date = DateField('Date of birth', validators=[DataRequired()])
    end_date = DateField('Date of birth', validators=[DataRequired()])
