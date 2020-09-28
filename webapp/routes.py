from webapp import app
from flask import render_template, redirect, url_for, request, jsonify, make_response
import re

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result', methods=["POST"])
def result():
    # transform input from text area into list
    req = request.get_json()
    as_list = req['input'].split()

    # remove dots
    no_dots = []

    for email in as_list:
        clean = re.sub("\.", "", email)
        no_dots.append(clean)

    # remove anything between + and @
    final = []

    for email in no_dots:
        cleaner = re.sub("\+spam", "", email)
        final.append(cleaner)

    # remove duplicates by converting clean list into set
    nodups = set(final)

    # count unique emails
    num = len(nodups)
    res = make_response(jsonify(num))
    return res
    return render_template("home.html")