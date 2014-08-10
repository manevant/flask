from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)





@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login2():
    form = LoginForm()

    if request.method == 'GET':
        if g.user and g.user.is_authenticated():
            return redirect(url_for('index'))
        return render_template('login.html', 
                            title = 'Sign In v2',
                            form = form)
    
    #IF POST METHOD
    if form.validate_on_submit():
        flash(str(form.data))
        return redirect(url_for('index'))

    return render_template('login.html', title = 'Sign In v2', form = form)
    






@app.route('/login2', methods = ['GET', 'POST'])
#@oid.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated():
      return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
  return render_template('login.html', 
      title = 'Sign In',
      form = form,
      providers = app.config['OPENID_PROVIDERS'])

