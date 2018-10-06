from flask import Flask, redirect, render_template, session, request
from mysqlconnection import connectToMySQL
from datetime import datetime
app=Flask(__name__)

@app.route('/')
def initialize():
	mysql = connectToMySQL('clientsdb')
	all_clients = mysql.query_db('SELECT clients.client, clients.leads FROM clients')
	return render_template('index.html', all_clients=all_clients)

@app.route('/update', methods=['POST'])
def update():
	mysql = connectToMySQL('clientsdb')
	client = mysql.query_db('SELECT client FROM clients')
	if client.updated_at < request.form['beginning']:
		if client.updated_at > request.form['end']:
			return redirect('/', client=clients, lead=leads)
	client = mysql.query_db(query,data)
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)