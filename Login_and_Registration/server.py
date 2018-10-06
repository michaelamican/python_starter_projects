from flask import Flask, session, request, render_template, redirect, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key='jigglypuff'
bcrypt = Bcrypt(app)

@app.route('/')
def initialize():
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	mysql = connectToMySQL('loginregdb')
	query = 'SELECT * FROM users where user = %(user)s'
	if len(request.form['password']) <1:
		flash('Please enter a password')
		return redirect('/')
	elif len(request.form['password']) <8:
		flash('Password must be at least 8 characters')
		return redirect('/')
	pass_hash = bcrypt.generate_password_hash(request.form['password'])
	data = {
		'user': request.form['user']
	}
	results = mysql.query_db(query, data)
	print(results)
	if len(results) < 1:
		flash('Username does not exist. Please register.')
		return redirect('/')
	else:
		user = results[0]
		password_test = bcrypt.check_password_hash(user['password'], request.form['password'])
		if not password_test:
			flash('Email does not match password. Please try again.')
			return redirect('/')
		else:
			session['user_id'] = user['id']
			return redirect('/welcome')

	return redirect('/')

@app.route('/create_user', methods=['POST'])
def create():
	mysql = connectToMySQL('loginregdb')
	errors = False
	query = 'SELECT * FROM users where user = %(user)s'

	query = 'INSERT INTO users (user, password, email, first_name, last_name, created_at, updated_at) VALUES (%(username)s, %(pw_hash)s, %(email)s, %(first_name)s, %(last_name)s, (NOW(), NOW());'

		# New User Registration
	mysql = connectToMySQL('loginregdb')
	if len(request.form['first_name']) < 1:
		errors = True
		flash('Please enter a first name')
	if len(request.form['last_name']) < 1:
		errors = True
		flash('Please enter a last name')
	if len(request.form['user']) < 8:
		errors = True
		flash('Must be at least 8 characters')
	if len(request.form['email']) < 1:
		errors = True
		flash('Please enter an email')
	elif not EMAIL_REGEX.match(request.form['email']):
		errors = True
		flash('Please enter a valid email')
	if len(request.form['password']) < 8:
		errors = True
		flash('Must be at least 8 characters')
	if not request.form['password'] == request.form['conpass']:
		errors = True
		flash('Confirmation must match password')
	if errors:
		flash('Something went wrong. See above')
		return redirect('/')
	else:
		pass_hash = bcrypt.generate_password_hash(request.form['password'])
		mysql = connectToMySQL('loginregdb')
		query = 'INSERT INTO users (user, first_name, last_name, password, email, created_at, updated_at) VALUES (%(user)s, %(first_name)s, %(last_name)s, %(password)s, %(email)s, NOW(), NOW());'
		data={
		'user': request.form['user'],
		'first_name':request.form['first_name'],
		'last_name': request.form['last_name'],
		'password': pass_hash,
		'email': request.form['email']
		}
		mysql.query_db(query, data)
		flash('Welcome to our community!')
		return redirect('/welcome')
	return redirect('/')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/guest')
def guest():
	return render_template('guest.html')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)