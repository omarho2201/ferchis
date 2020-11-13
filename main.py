from flask import Flask, render_template, request, session, logging, url_for,redirect,json,flash
app = Flask(__name__)

@app.route("/")
def inicio():   
    return redirect(url_for("encuesta"))

@app.route("/encuesta", methods=["GET","POST"])
def encuesta():
    if request.method=="POST":
        return redirect(url_for("medijoquesi"))
    return render_template("encuesta.html")

@app.route("/medijoquesi", methods=["GET","POST"])
def medijoquesi():

    return render_template("medijoquesi.html")


if __name__=="__main__":
    app.run(debug=True)