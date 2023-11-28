from flask import Blueprint, render_template, request, redirect, url_for, abort, session
from jinja2 import TemplateNotFound

from controller.character_controller import PlayerController

create_character = Blueprint('create_character', __name__,
                             template_folder='templates',
                             static_folder='static'
                             )


@create_character.route('/character_form', defaults={'page': 'character_form'}, methods=['GET'])
def character_form(page):

    if 'player_controller' not in session.keys():
        try:
            return redirect(url_for('home.welcome'))
        except TemplateNotFound:
            abort(404)

    player_controller: PlayerController = session['player_controller']
    race_bean = player_controller.race_bean
    list_races = race_bean.races
    list_classes = PlayerController.get_classes()
    print(list_races)
    try:
        return render_template(f'{page}.html', list_races=list_races, list_classes=list_classes)
    except TemplateNotFound:
        abort(404)


@create_character.route('/character_form', methods=['POST'])
def create_character_form():
    char_name = request.form.get('char_name')
    char_class = request.form.get('class')
    char_race = request.form.get('race')
    char_background = request.form.get('background')
    char_alignment = request.form.get('alignment')
    char_level = request.form.get('level')

    # Esegui qui le operazioni necessarie per salvare il personaggio

    # Ad esempio, puoi stampare le informazioni del personaggio
    print(f"Character Name: {char_name}")
    print(f"Class: {char_class}")
    print(f"Race: {char_race}")
    print(f"Background: {char_background}")
    print(f"Alignment: {char_alignment}")
    print(f"Level: {char_level}")

    # Puoi anche aggiungere la logica per salvare il personaggio nel tuo sistema

    # Redirect alla pagina di conferma o ad altre pagine dopo la creazione del personaggio
    return redirect(url_for('create_character.show_create_character_form'))
