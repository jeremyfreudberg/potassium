from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms import IntegerField, RadioField
from wtforms.validators import DataRequired


class Nutrition(Form):
    food = StringField('Food: ', validators=[DataRequired()])
    element = RadioField('Element: ', choices=[('potassium','Potassium'), ('sodium','Sodium')],\
                         validators = [DataRequired()],\
                         default='k')
    amount = IntegerField('Amount: ', validators=[DataRequired()])
    unit = SelectField('(Unit)', choices=[('ounces','Ounces'),\
                                        ('pounds','Pounds'),\
                                        ('teaspoons','Teaspoons'), \
                                        ('tablespoons', 'Tablespoons')],\
                       validators=[DataRequired()])
    submit= SubmitField('Submit')
