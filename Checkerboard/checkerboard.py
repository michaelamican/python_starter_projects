from flask import Flask, render_template

app = Flask(__name__)
print (__name__)

@app.route('/')
def lets_play(row=8,col=8):
	row = 8
	col = 8
	return render_template("index.html",row=row,col=col)


@app.route('/<row>/<col>')
def lets_play_more(row="",col=""):
	row = int(row)
	col = int(col)
	return render_template("index.html",row=row,col=col)

if __name__=='__main__':
	app.run(debug=True)