from flask import Flask, render_template, request, redirect

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
    name = request.form.get('name')
    options = request.form.get('options')
    if not name or not options:
        return render_template('failure.html')
    users.append(f'{name} selected {options}')
    return redirect('/registrants')