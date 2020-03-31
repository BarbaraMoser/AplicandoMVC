from flask import Blueprint, render_template, request, redirect

from app.controllers.user_controller import UserController

app_cadastro = Blueprint('app.cadastro', __name__, template_folder='templates')


@app_cadastro.route('/cadastros')
def cadastro():
    return render_template('cadastro.html')


@app_cadastro.route('/salvar_cadastro', methods=['POST'])
def salvar_cadastro():
    try:
        UserController.create(
            username=request.form['username'],
            password=request.form['password'],
            email=request.form['email'],
            fullname=request.form['name'],
            gender=request.form['gender'],
            contact_number=request.form['number'],
            address=request.form['location'],
        )
        return redirect('/access_allowed')
    except:
        return redirect('/access_denied')
