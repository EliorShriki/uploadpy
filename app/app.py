from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from os.path import dirname, join
from . import logging, logger #pylint: disable=relative-beyond-top-level
import os
import importlib
import sys
import shutil
from . import helper #pylint: disable=relative-beyond-top-level

upload_folder = 'uploads'
secret_key = 'shh_this_is_top_secret'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['SECRET_KEY'] = secret_key

wd40 = os.getcwd()
sys.path.insert(0, wd40 + "\\uploadpy\\modules")
queries = helper.load_queries()
taalichim = helper.get_taalichim(queries)

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/logs')
def logs():
    pass

def verify():
    try:
        pro_name = session['procedure_name']
        mod = importlib.import_module(pro_name)
        helper.run_task(mod, pro_name)
        return redirect(url_for('load'))
    except:
        return redirect(url_for('error'))

@app.route('/data', methods=['GET', 'POST'])
def data():
    try:
        tables = session['tables']
        procedure_name = session['procedure_name']
        if request.method == 'POST':
            return verify()
        else:
            return render_template('data.html', tables=tables, procedure_name=procedure_name)
    except:
        return redirect(url_for('error'))

@app.route('/', methods=['GET', 'POST'])
@app.route('/load', methods=['GET', 'POST'])
def load():
    try:
        if request.method == 'POST':
            files = request.files.getlist('files')
            procedure_name = request.form.get('taalichim')
            mod = importlib.import_module(procedure_name)
            tables = []
            for f in files:
                directory = join(dirname(dirname(__file__)), upload_folder)
                f.save(join(directory, f.filename))
                tables.append(helper.load_df(f))
            if mod.check_input():
                session['tables'] = tables
                session['procedure_name'] = procedure_name
                return redirect(url_for('data'))
            else:
                return redirect(url_for('error'))
        else:
            return render_template('load.html', taalichim=taalichim)
    except:
        return redirect(url_for('error'))

def run(is_debug=True):
    app.run(is_debug)
    return 1