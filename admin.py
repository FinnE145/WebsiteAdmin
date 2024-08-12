import sys
import requests
from multiprocessing import Process
from flask import Flask, render_template, request

app = Flask(__name__)

print("Running admin")

# Import the code for the main server - main server is in a different directory
sys.path.append("C:/Users/finne/OneDrive/Documents/0coding/FEWebsite")
import app as mainServer

# Start the main server process
server = Process(target=mainServer.run)
server.daemon = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    print("Test from admin")
    return "test"

@app.route("/restart", methods=["GET", "POST"])
def restart():
    # Check which branch was updated
    res = request.get_json()
    branch = res["ref"].split("/")[-1]
    print(f"Committed to {branch}")
    if branch == "main":
        print("Main branch updated, restarting")

        # Stop the server process
        global server
        global mainServer
        server.terminate()
        server.join()

        # Ensure it has been stopped
        try:
            reqRes = requests.get("http://127.0.0.1:5000/test")
            print(f"Main server is still running ({reqRes.status_code})")
            raise AssertionError("Main server is still running")
        except requests.exceptions.ConnectionError:
            print("Main server has stopped")

        # Not sure if this is necessary
        del mainServer

        # TODO: git pull

        # Import the new code
        import app as mainServer

        # Start the server process
        server = Process(target=mainServer.run)
        server.daemon = True
        server.start()

        return "Server restarted"
    else:
        print("Main branch not updated, nothing to do")
        return "Server not restarted due to incorrect branch"

if __name__ == "__main__":
    server.start()
    app.run(port=5001)
