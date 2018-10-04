from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route("/")
def index():
	id = 3
	color = "cornflowerblue"
	return render_template("index.html",id=id,color=color)


@app.route("/play/<id>")
def route2(id):
	id = int(id)
	color= "cornflowerblue"
	return render_template("index.html",id=id,color=color)

@app.route("/play/<id>/<color>")
def route3(id, color):
	id = int(id)
	return render_template("index.html",id=id,color=color)

if __name__=="__main__":
	app.run(debug=True)
