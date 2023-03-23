from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"


@app.route("/")
def home():
    return jsonify({'Message': "Nne"})


if __name__ == "__main__":
    app.run()
