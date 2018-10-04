from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/hey_gurl_hey")
def hey_gurl_hey():
	print("hey_gurl_hey route")
	return "Hello World!"

@app.route("/dojo")
def dojo():
	print("dojo route")
	return "Dojo!"

@app.route("/say/<name>")
def say(name):
	print("Say route")
	return "Hi "+name
@app.route("/repeat/<number>/<word>")
def repeat(number, word):
	print("Repeat")
	return int(number)*(word)

if __name__=="__main__":
	app.run(debug=True)