from flask import  Flask, render_template, redirect, request
from werkzeug.utils import secure_filename
import  pandas as pd
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':            
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html') 

        f = request.files['file']

        # if user does not select file, browser also
        if f and f.filename != '' and allowed_file(f.filename):            
            dirname = os.path.join(os.path.dirname(os.path.dirname(__file__)),UPLOAD_FOLDER)
            f.save(os.path.join(dirname,f.filename))
            data_xls = pd.read_excel(f)
            return render_template('data.html', data=data_xls.to_html(header=True, index=False))              
        return render_template('index.html')
def run(is_debug=True):    
    app.run(debug=is_debug)