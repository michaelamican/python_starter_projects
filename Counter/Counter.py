from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key='Jigglypuff'

@app.route('/')
def index():
	if not 'count' in session:
		session['count'] = 0
	else:
		session['count'] += 1
	print(session['count'])
	return render_template('index.html')

@app.route('/refresh')
def add2():
	session['count'] = int(session['count']) + 1
	return redirect('/')

@app.route('/destroy_session')
def reset():
	session['count'] = 0
	print(session['count'])
	return redirect('/')


if __name__=="__main__":
	app.run(debug=True)