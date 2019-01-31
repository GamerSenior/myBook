from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('index.html')

@main.errorhandler(404)
def page_not_found(e):
    return "Pagina não encontrada"