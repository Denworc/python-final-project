"""

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
# from markupsafe import Markup


class DepartmentForm(FlaskForm):
    """

    """
    name = StringField('Department name', validators=[DataRequired(), Length(min=0, max=50)])
    # submit_value = Markup("<i class='icon-user-follow'></i> New")
    # submit = SubmitField(default = submit_value)
