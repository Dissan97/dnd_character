from flask import Blueprint, render_template, redirect, abort, session, url_for
from jinja2 import TemplateNotFound

from bean.player_beans import PlayerBean
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
        player_bean: PlayerBean = player_controller.get_player_bean()
        session['player_controller'] = player_controller
        print(player_bean.get_name())
        if player_bean is not None:
            try:
                return render_template(f'{page}.html', player_name=player_bean.get_name())
            except TemplateNotFound:
                abort(404)
        else:
            try:
                return render_template(url_for('login.sign_in', error="UNKNOWN"))
            except TemplateNotFound:
                abort(404)
