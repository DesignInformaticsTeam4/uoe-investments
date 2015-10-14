#!/usr/bin/python
# coding: utf-8
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, \
    render_template, flash, Response, send_file
# from domain_getter import domainify
import json
import pickle
import random

app = Flask(__name__)
app.config.from_object(__name__)
app.config['STATIC_FOLDER'] = os.getcwd()
cfg = None

# with open('data_large_new.json') as data_file:
#         data = json.load(data_file)
        # for i in data['investments']:
        #     print(i)

data = pickle.load(open('data_pickle.pkl', 'r'))

def get_random():
    i = random.randint(0,len(data))
    return data['investments'][5]

@app.route('/')
def name_me():
    domain = get_random()
    return render_template('talktome.html', domain=domain)


if __name__ == "__main__":
    app.run(debug=True)
