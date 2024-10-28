# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Hello, {name}!"
    return render_template("index copy.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
