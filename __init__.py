from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"


@app.route("/")
def home():
    return jsonify({'Message': "None"})


@app.route("/main")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
