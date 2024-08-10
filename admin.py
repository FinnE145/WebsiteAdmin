from flask import Flask, render_template, request

app = Flask(__name__)

print("Running admin")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/restart", methods=["GET", "POST"])
def restart():
    print(request.form)
    return "Nothing happened"

if __name__ == "__main__":
    app.run()
