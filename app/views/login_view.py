from flask import Blueprint, render_template, request, redirect

from app.controllers.login_controller import LoginController

app_login = Blueprint('app.login', __name__, template_folder='templates')


@app_login.route('/start')
def login():
    return render_template('login.html')


@app_login.route('/logins', methods=['POST'])
def save_login():
    try:
        login_controller = LoginController()
        username = request.form['username']
        password = request.form['password']
        login_controller.validate_login(username, password)
        return redirect('/access_allowed')
    except:
        return redirect('/access_denied')


@app_login.route('/access_allowed')
def access_allowed():
    return render_template('acesso_permitido.html')


@app_login.route('/access_denied')
def access_denied():
    return render_template('acesso_negado.html')
