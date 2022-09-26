from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request, session, render_template_string
from flask_bootstrap import Bootstrap

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from numpy import identity

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "iO1K3FqsIFnQ7n3e1eQx3L7I2JVdMXaZO8PAdqLl"

app.config["JWT_SECRET_KEY"] = "emNtAK1iFSzr2yOV4N1a4ebPojVU2CV6fIhhIrJT"
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

jwt = JWTManager(app)

#setup sqlite

@app.route("/")
def index():
    """list all challenges"""
    return render_template("index.html")

@app.route("/xss1")
def xss1():
    """alert the cookie via reflected"""
    return None

@app.route("/xss2")
def xss2():
    """alert the cookie via stored + redirect user to their page"""
    return None

@app.route("/sqli1")
def sqli1():
    """SQLi to login"""
    return None

@app.route("/sqli2")
def sqli2():
    """SQLi to dump creds"""
    return None

@app.route("/jwt")
def jwt():
    """edit JWT to bypass
    clear cookie after"""
    return None

@app.route("/idor")
def idor():
    """IDOR challenge view admin password
    renders a profile page based on endpoint param"""
    return None

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
    # app.run(host="0.0.0.0", port=80)