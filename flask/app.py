from flask import Flask
import os
import socket
app = Flask(__name__)

@app.route("/")
def hello():
    name=str(os.environ["NAME"])
    return "Hello {}. Welcome to Docker! From your Friend, {}!".format(name, socket.gethostbyname(socket.gethostname()))

@app.route("/http-normal")
def http():
    return "Successfully accessed normal HTTP!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
