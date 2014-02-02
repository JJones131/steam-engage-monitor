from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
    return redirect('/index')
  return render_template('login.html', 
    title = 'Sign In',
    form = form)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL. :(', 404
