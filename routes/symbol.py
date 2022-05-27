from flask import Blueprint, \
    render_template, \
    redirect, \
    url_for, \
    request, \
    flash
from models import Symbol
from app import db
from flask_login import current_user

symbol = Blueprint('symbol', __name__)

@symbol.route('/symbol')
def index():

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('symbol/index.html', models=Symbol.query.all())

@symbol.route('/symbol', methods=['POST'])
def store():

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    new_symbol = Symbol(symbol=request.form.get('symbol'))

    db.session.add(new_symbol)
    db.session.commit()

    flash('{} just created.'.format(new_symbol.symbol))
    
    return redirect(url_for('symbol.create'))

@symbol.route('/symbol/create')
def create():

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
        
    return render_template('symbol/create.html')
