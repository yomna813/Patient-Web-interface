from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,EmailField,DateField
from wtforms.validators import DataRequired,length,Email,EqualTo

class Signup(FlaskForm):
    
    username= StringField('username',validators=[DataRequired(),length(max=20)])
    email=EmailField("Email",validators=[DataRequired()])
    password= PasswordField('password',validators=[DataRequired(),length(max=20,min=3)])
    Re_password= PasswordField('confirm_password',validators=[DataRequired(),EqualTo("password",message='password didnt match')])
    Fname= StringField('First name',validators=[DataRequired(),length(max=10)])
    Lname= StringField('Last name',validators=[DataRequired(),length(max=10)])
    NID = StringField('National ID',validators=[DataRequired()])
    BD = DateField('BirthDate',format='%Y-%m-%d')
    submit= SubmitField('submit')

class Search(FlaskForm):
    NID = StringField('National ID',validators=[DataRequired()])
    submit= SubmitField('submit')

