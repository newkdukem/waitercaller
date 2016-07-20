from flask import Flask
from flask import render_template
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from mockdbhelper import MockDBHelper as DBHelper
from user import User
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.secret_key = 'zV+ftkCCiWBYvFO/WHkj7UiRhmIvRZi2PFk4xw04SkRLzFkYm2ZSDDEA6E/nAXuzwKU+zYN8/Exx2UcdrRY65VOKgG+e73qbCWM'
login_manager = LoginManager(app)
DB = DBHelper()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/account")
@login_required
def account():
    return "You are logged in"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
