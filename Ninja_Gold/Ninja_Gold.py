from flask import Flask, render_template, session, request, redirect
app=Flask(__name__)
app.secret_key='jigglypuff'

@app.route('/')
def walk():

	if 'gold' not in session:
		session['gold'] = 0
	if 'action' not in session: 
		session['action'] = []
	if 'action' in session:
		session['action'].append("Earned" + str(session['gold']) + "gold!")
	return render_template('index.html', gold = session['gold'], action=session['action'])

@app.route('/process_money', methods=['POST'])
def process():
	import random
	import datetime

	if 'gold' not in session:
		session['gold'] = 0
	if 'farm' in request.form:
		session['gold'] += random.randrange(9,21)
	elif 'cave' in request.form:
		session['gold'] += random.randrange(4,11)
	elif 'house' in request.form:
		session['gold'] += random.randrange(1,6)
	elif 'casino' in request.form:
		session['gold'] += random.randrange(-51,51)
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)