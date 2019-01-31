from flask import Flask, url_for
from .main.views import main
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.register_blueprint(main)

"""
Sempre que for chamada a função url_for, sera feito o append
com o timestamp da ultima modificação do arquivo, caso for estático
"""
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)