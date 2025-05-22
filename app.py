

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello!</h1><p>New videos will be uploaded soon.</p>"


if __name__ == "__main__":
    app.run(debug=True)
