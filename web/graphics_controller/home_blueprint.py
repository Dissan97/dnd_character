from flask import Blueprint, render_template, after_this_request, g

home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static'
                 )


@home.route('/', defaults={'page': 'home'})
@home.route('/')
def welcome():
    return render_template('home.html')
