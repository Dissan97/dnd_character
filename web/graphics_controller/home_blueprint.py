from flask import Blueprint, render_template, after_this_request, g

home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static'
                 )

page = 'character_sheet'
@home.route('/', defaults={'page': f'{page}'})
@home.route('/')
def welcome():
    return render_template('character_sheet.html')
