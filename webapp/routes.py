from webapp import app
from flask import request, jsonify
import re

@app.route('/')
def home():
    return jsonify(status='ok')

@app.route('/dedup_emails', methods=["POST"])
def result():
    # transform input into list
    req = request.get_json()
    as_list = req['input'].split()

    # remove dots after @
    no_dots = []

    for email in as_list:
        clean = re.sub("\.((?!com))", "", email)
        no_dots.append(clean)

    # remove anything between + and @
    final = []

    for i in no_dots:
        cleaner = re.sub("(?=\+).*?(?=\@)", "", i)
        final.append(cleaner)
        
    # remove duplicates by converting final list into set
    nodups = set(final)

    # count unique emails
    num = len(nodups)
    return jsonify(f"Total number of unique, valid email addresses: {num}.")