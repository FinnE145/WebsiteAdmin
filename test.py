import sys
import requests
from multiprocessing import Process

if __name__ == "__main__":
    # sys.path.append("C:/Users/finne/OneDrive/Documents/0coding/FEWebsite")
    # import app

    # server = Process(target=app.run)
    # server.start()
    # res = requests.get("http://127.0.0.1:5000/testDB")
    # print(res.status_code)
    # server.terminate()
    # server.join()

    try:
        res = requests.get("http://127.0.0.1:5000/test")
        print("App:", res.status_code)
    except requests.exceptions.ConnectionError:
        print("Main server has stopped")
    
    try:
        res = requests.get("http://127.0.0.1:5001/test")
        print("Admin:", res.status_code)
    except requests.exceptions.ConnectionError:
        print("Main server has stopped")
    
    while True:
        try:
            urlStr = f"http://127.0.0.1:{(p:=input('Enter port: '))}/{(r:=input('Enter route: ').strip('/'))}"
            res = requests.get(urlStr)
            if res.status_code == 415:
                res = requests.post(urlStr, json={"ref": "refs/heads/main"})
            print(f"Server at {p}/{r}:", res.status_code)
            print(res.text)
        except requests.exceptions.ConnectionError:
            print(f"Server at {p} has stopped")
        except requests.exceptions.InvalidURL:
            print("Invalid URL")
        except KeyboardInterrupt:
            break