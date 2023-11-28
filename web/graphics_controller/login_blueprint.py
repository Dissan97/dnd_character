from flask import Blueprint, render_template, request, redirect, url_for, abort, g, after_this_request, session
from jinja2 import TemplateNotFound
from controller.login_controller import Login
import flask_session
login = Blueprint('login', __name__,
                  template_folder='templates',
                  static_folder='static')


@login.route('/sign_in', defaults={'page': 'sign_in'})
def sign_in(page):

    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)


@login.route('/sign_in', methods=['POST'])
def sign_in_confirm():
    username = request.form.get('username')
    password = request.form.get('password')

    login_controller = Login()

    # For simplicity, let's just check if both are 'admin' for demonstration purposes
    if login_controller.sign_in(username, password) > -1:
        session['login_controller'] = login_controller
        return redirect(url_for('player_home.player_home_page'))
    else:
        # Redirect back to the login page with an error parameter
        return redirect(url_for('login.sign_in', error=login_controller.error_message))


@login.route('/sign_up', defaults={'page': 'sign_up'})
def sign_up(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)


@login.route('/sign_up', methods=['POST'])
def sign_up_confirm():
    login_controller = Login()
    username = request.form.get('username')
    password = request.form.get('password')

    # Here, you can perform any logic to validate the username and password
    # For simplicity, let's just check if both are 'admin' for demonstration purposes
    if login_controller.sign_up(username, password) > -1:
        return redirect(url_for('login.sing_in'))
    else:
        # Redirect back to the login page with an error parameter
        return redirect(url_for('login.sign_up', error=login_controller.error_message))
