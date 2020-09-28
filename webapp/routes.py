from webapp import app
from flask import render_template, redirect, url_for, request, jsonify, make_response
import re

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result', methods=["POST"])
def result():
    req = request.get_json()
    as_list = req['input'].split()

    clean_list = []

    for email in as_list:
        clean = re.sub('\.', "", email)
        clean_list.append(clean)

    nodups = set(clean_list)
    print(nodups)

    num = len(nodups)
    res = make_response(jsonify(num))
    return res
    return render_template("home.html")