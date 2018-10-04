
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    sberry = int(request.form['quantity_strawberry'])
    rberry = int(request.form['quantity_raspberry'])
    apple = int(request.form['quantity_apple'])
    bberry = int(request.form['quantity_blackberry'])
    name = request.form['name']
    StudID = int(request.form['StudID'])
    count = (sberry + rberry + apple + bberry)
    return render_template("checkout.html", sberry=sberry, rberry=rberry, apple=apple, bberry=bberry, name=name, StudID=StudID, count=count)

if __name__=="__main__":   
    app.run(debug=True)   