from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
# from markupsafe import Markup


class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=0, max=50)])
    department_id = SelectField('Department', validators=[DataRequired(), Length(min=0, max=50)])
    date_of_birth = StringField('Date of birth', validators=[DataRequired(), Length(min=0, max=50)])
    salary = StringField('Salary', validators=[DataRequired(), Length(min=0, max=50)])
    # submit_value = Markup("<i class='icon-user-follow'></i> New")
    # submit = SubmitField(default = submit_value)
