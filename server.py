from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def blog_front_paige():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)