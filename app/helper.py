import json
import os
import cx_Oracle as ora
import pandas as pd
import shutil

os.environ['NLS_LANG'] = '.al32utf8'
wd40 = os.getcwd()
queries_path = wd40 + '\\uploadpy\\app\\queries.json'
connector = ora.connect('RM', 'L0ND0N', 'OFEK.WORLD')
upload_folder = 'uploads'

def load_queries():
    queries_json = {}
    data = {}
    with open(queries_path, 'r', encoding='utf8') as queries:
        queries_json = json.load(queries)
    for i in queries_json:
        data[i['query_id']] = i['query']
    return data

def get_taalichim(queries):
    taalichim = []
    taalichim_t = []
    with connector.cursor() as c:
        c.execute(queries['1'])
        taalichim_t = c.fetchall()
    for row in taalichim_t:
        taalichim.append({'id': row[0], 'name': row[1]})
    return taalichim

def load_df(f):
    file_type = f.filename.split('.')[1]
    df = None
    if file_type in ['xlsx', 'xls']:
        df = pd.read_excel(f).head(3)
    if file_type in ['csv']:
        df = pd.read_csv(f).head(3)
    df.style.set_caption(f.filename)
    return df.to_html(classes=['table-bordered', 'table-light', 'table-hover', 'table-striped'])