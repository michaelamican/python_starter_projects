from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key='Mine'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/created_at', methods=['POST'])
def create_user():
	session['text'] = request.form['text']
	session['campus'] = request.form['campus']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	return redirect('/result')

@app.route('/result')
def show_user():
	return render_template('created_at.html')

@app.route('/danger')
def notredirect():
	print("Molly, you in danger girl")
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)