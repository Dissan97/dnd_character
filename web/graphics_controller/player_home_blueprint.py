from flask import Blueprint, render_template, redirect, abort, session
from jinja2 import TemplateNotFound

from controller.character_controller import PlayerController
from controller.login_controller import Login

player_home = Blueprint('player_home', __name__,
                        template_folder='templates',
                        static_folder='static')


@player_home.route('/player_home', defaults={'page': 'player_home'})
def player_home_page(page):
    if 'player_controller' not in session.keys():
        login_controller: Login = session.get('login_controller')
        player_controller = PlayerController(login_controller)
        session['player_controller'] = player_controller
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)
