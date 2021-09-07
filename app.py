from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
#there are as many inexes as one can see

if __name__ == '__main__':
    app.run()