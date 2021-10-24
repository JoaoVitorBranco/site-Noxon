from flask import Flask, redirect, url_for, render_template, request
from momento import momento_inercia
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def entrada():
    if request.method == "POST":
        l = request.form["l"]
        t = request.form["t"]
        leg = request.form["leg"]
        n = request.form["n"]
        m = request.form["m"]
        
        return redirect(url_for("user", l=l, t=t, leg=leg, n=n, m=m))
    else:  
        return render_template("entrada.html")

@app.route('/user/<float:l>,<float:t>,<float:leg>,<float:n>,<float:m>')
def user(l,t,leg,n,m):
    mi = momento_inercia(l,t,leg,n,m)

    return f"<p>O Momento de Inércia é: {mi:.2f} m⁴</p>"


if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)