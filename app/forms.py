from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators
#from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', [validators.DataRequired()])
    password = PasswordField('New Password', [validators.DataRequired()])
    remember_me = BooleanField('remember_me', default = False)