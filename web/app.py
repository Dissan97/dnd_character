from flask import Flask, session

from controller.utils import extract_enums_list
from dao.race_loader import extract_races
from flask_session import Session
from controller.session import SessionManager
from graphics_controller.create_character import create_character
from graphics_controller.login_blueprint import login
from graphics_controller.home_blueprint import home
from graphics_controller.player_home_blueprint import player_home
from model.character import ClassType

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# Register the blueprints
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(player_home)
app.register_blueprint(create_character)


if __name__ == '__main__':

    app.run(debug=True)
