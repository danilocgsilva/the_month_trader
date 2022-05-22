from flask import Blueprint
from flask import render_template

symbol = Blueprint('symbol', __name__)

@symbol.route('/symbol')
def index():
    return render_template('symbol/index.html')

@symbol.route('/symbol/create')
def create():
    return render_template('symbol/create.html')
