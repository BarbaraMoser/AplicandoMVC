from flask import Blueprint, render_template

app_start = Blueprint('app.start', __name__, template_folder='templates')


@app_start.route('/')
def start():
    return render_template('index.html')
