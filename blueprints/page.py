from flask import Blueprint,  render_template
page = Blueprint('page', __name__)



@page.route('/')
def home():
    return render_template("home.html")


@page.route('/lista_email')
def lista_email():
    return render_template("lista_email.html")