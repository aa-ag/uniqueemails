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
    as_list = req['csvEmails'].split()

    # remove dots before @
    no_dots = []

    for email in as_list:
        clean = re.sub("\.((?!com))", "", email)
        no_dots.append(clean.replace(",", ""))

    # remove anything between + and @
    final = []

    for i in no_dots:
        cleaner = re.sub("(?=\+).*?(?=\@)", "", i)
        final.append(cleaner)

    # single regex
    # [!] if top-level domain has two to six letters (thirdlevel.secondlevel.com)
    # ^[\w!#$%&'*+/=?`{\}~^-]+(?:\.[\w!#$%&'*+/=?`{|}~^-]+*@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$

    # remove duplicates by converting final list into set
    nodups = set(final)

    # count unique emails
    num = len(nodups)
    return jsonify(totalNumberOfUniqueEmails=num)
