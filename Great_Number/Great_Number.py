from flask import Flask, session, request, render_template, redirect
app=Flask(__name__)
app.secret_key="jigglypuff"

@app.route('/')
def show():
	import random
	session['num'] = random.randrange(0,101);
	number = session['num']
	print(number)
	return render_template("index.html")

@app.route('/evaluating', methods=['POST'])
def evaluating():
	guess = int(request.form['bar'])
	number = session['num']
	if guess < number:
		return render_template('low.html', guess=guess)
	elif guess > number:
		return render_template('high.html', guess=guess)
	else:
		return render_template('correct.html', guess=guess)


@app.route('/reset', methods=['POST'])
def correct():
	session.clear()
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)