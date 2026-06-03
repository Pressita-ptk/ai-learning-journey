from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/academic")
def academic():
    return render_template("academic.html")

@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/timeline")
def timeline():
    return render_template("timeline.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)