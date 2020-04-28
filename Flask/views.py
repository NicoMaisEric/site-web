from flask import Flask , render_template
from flask import request

app = Flask ( __name__ )

@app.route ('/')
def index():
    return render_template("index.html")
@app.route('/raoult')
def raoult():
    return render_template("raoult.html")
@app.route('/formulaire', methods = ['POST'])   
def formulaire():  
    result = request.form
    n = result['nom']
    p = result['prénom']
    c = result['codecb']
    return render_template("formulaire.html", nom=n, prenom=p, codecb=c)
@app.route('/calculatrice')
def calculatrice():
    return render_template("calculatrice.html")
app.run(debug=False)