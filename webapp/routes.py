from webapp import app
from flask import render_template, redirect, url_for, request, jsonify, make_response

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result', methods=["POST"])
def result():
    req = request.get_json()
    as_string = req['input'].split()
    num = len(as_string)
    res = make_response(jsonify(num))
    return res
    return render_template("home.html")