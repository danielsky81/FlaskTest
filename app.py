from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Register User
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrants')
def registrants():
    return render_template('registrants.html', users=users)

@app.route('/register', methods=['POST'])
def register():
    if not request.form.get('name') or not request.form.get('options'):
        return render_template('failure.html')
    file = open('registered.csv', 'a')
    writer = csv.writer(file)
    writer.writerow((request.form.get('name'), request.form.get('options')))
    file.close()
    return render_template('success.html')

@app.route('/registered')
def refistered():
    file = open('registered.csv', 'r')
    reader = csv.reader(file)
    users = list(reader)
    return render_template('registered.html', users=users)