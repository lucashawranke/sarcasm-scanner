from flask import Flask
import pickle

app = Flask(__name__)

filename = "model.pkl"
# model = joblib.load(filename)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()