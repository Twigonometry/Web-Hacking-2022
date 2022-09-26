from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request, session, render_template_string
from flask_bootstrap import Bootstrap

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from numpy import identity

import random

import string

import sqlite3

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "iO1K3FqsIFnQ7n3e1eQx3L7I2JVdMXaZO8PAdqLl"

app.config["JWT_SECRET_KEY"] = "emNtAK1iFSzr2yOV4N1a4ebPojVU2CV6fIhhIrJT"
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

jwt = JWTManager(app)

current_sessions = []

#setup sqlite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    """list all challenges"""
    if "userid" not in session:
        tmp_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

        while tmp_id in current_sessions:
            tmp_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

        session["userid"] = tmp_id

    return render_template("index.html")

@app.route("/xss1")
def xss1():
    """alert the cookie via reflected"""
    if request.args.get("flavour") and request.args.get("quantity"):
        return render_template("xss1.html", order=True, flavour=request.args.get("flavour"), quantity=request.args.get("quantity"))
    else:
        return render_template("xss1.html")

@app.route("/xss2")
def xss2():
    """alert the cookie via stored + redirect user to their page"""
    conn = get_db_connection()
    comments = conn.execute("SELECT * FROM posts WHERE userid = ?", session["userid"]).fetchall()
    return render_template("xss2.html", comments=comments)

@app.route("/xss2/comment", methods=["POST"])
def insert_comment():
    """insert a comment"""
    conn = get_db_connection()
    return redirect("/xss2")

@app.route("/sqli1")
def sqli1():
    """SQLi to login"""
    return render_template("sqli1.html")

@app.route("/sqli2")
def sqli2():
    """SQLi to dump creds"""
    return render_template("sqli2.html")

@app.route("/jwt")
def jwt():
    """edit JWT to bypass
    clear cookie after"""
    return render_template("jwt.html")

@app.route("/idor")
def idor():
    """IDOR challenge view admin password
    renders a profile page based on endpoint param"""
    return render_template("idor.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
    # app.run(host="0.0.0.0", port=80)