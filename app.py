from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy user data for demonstration
users = {
    "ravi": generate_password_hash("ravi123")
}


@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]}. <form action="/logout" method="post"><button type="submit">Logout</button></form>'
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username], password):
        session['username'] = username
        return redirect(url_for('home'))
    return 'Invalid username or password'


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
