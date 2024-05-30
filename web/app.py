from flask import Flask, render_template , request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/..", methods=["GET", "POST"])
def algo():
    if request.method == "POST":
        nombre = request.form.get("fname")
        email = request.form.get("email")
        mensaje = request.form.get("msj")
        return render_template("succesful_form.html", name=nombre, email=email,msg=mensaje)
    return render_template("base.html")


@app.route("/habitacion1")
def habitacion_1():
    return render_template("habitacion1.html")


@app.route("/habitacion2")
def habitacion_2():
    return render_template("habitacion2.html")


@app.route("/habitacion3")
def habitacion_3():
    return render_template("habitacion3.html")


if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)