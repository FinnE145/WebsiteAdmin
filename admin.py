from flask import Flask, render_template, request

app = Flask(__name__)

print("Running admin")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/restart", methods=["GET", "POST"])
def restart():
    res = request.get_json()
    print(res)
    branch = res["ref"].split("/")[-1]
    print(f"Committed to {branch}")
    if branch == "main":
        print("Main branch updated, restarting")
        return "Restarting"
    else:
        return "Nothing happened"

if __name__ == "__main__":
    app.run()
