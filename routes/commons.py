from flask_login import current_user
from flask import url_for, redirect

def hidden_to_logged():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))