from fileinput import filename
import json
import os.path
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'djbadbbhh1b32h3b2bsndsjjdns32jn2bh3h2'

@app.route('/')
def home():
    return render_template('home.html', name='Vishnu')

@app.route('/your-url',methods=[ 'GET','POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
              
        if request.form['code'] in urls.keys(): 
            flash('That shortname has already been taken. Please select another name')
            return redirect(url_for('home'))
        
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/Users/Admin/Documents/flask exercise files/Ex_Files_Flask_EssT/url-shortner/static/user_files/'+full_name)    
            urls[request.form['code']] = {'file':full_name}
        
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code = request.form['code'])
    else:
        return redirect(url_for('home'))
    
@app.route('/<string:code>') #any string entered is assigned to variable code
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as url_file:
            urls = json.load(url_file)
            
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static',filename='user_files/'+urls[code]['file']))