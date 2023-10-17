from flask import Flask, render_template, redirect
from sqlalchemy import create_engine
# from sqlalchemy.orm

app = Flask("__name__")

# engine = create_engine("sqlite:///chat.db", echo=True)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)