from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    name=str(os.environ["NAME"])
    return "Hello {}!".format(name)

@app.route("/http-normal")
def http():
    return "Successfully accessed normal HTTP!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)