from flask import Blueprint, render_template, request

from app.controllers.login_controller import LoginController

app_login = Blueprint('app.login', __name__, template_folder='templates')


@app_login.route('/')
def start():
    return render_template('login.html')


@app_login.route('/logins', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        LoginController.create(username, password)
        return 'deu certo'
    except:
        raise Exception('deu pauuuu')
