from flask import Flask, render_template, session, request, redirect, flash
app = Flask(__name__)
app.secret_key='Mine'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def create_user():

	session['username'] = request.form['username']
	session['campus'] = request.form['campus']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']

	if len(session['username']) < 8:
		flash("Username must be at least 8 characters")
	if session['campus'] == "nochoice":
		flash("Please select a campus")
	if session['language']=="nochoice":
		flash("Please select a language")
	if len(session['comment']) > 255:
		flash("Your comment must not exceed 255 characters")
	if '_flashes' in session.keys():
		flash(f"Something went wrong. See above.")
		return redirect('/')
	else:
		return redirect('/result')

@app.route('/result')
def show_user():
	return render_template('created_at.html')

@app.route('/confirm', methods=['POST'])
def login():
	return redirect('/welcome')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

if __name__=='__main__':
	app.run(debug=True)