from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/", methods=["GET", "POST"])
# def index():
#     return render_template("index.html")

def gfg(): # <-- THIS NAME HAS TO MATCH THE action="{{ url_for('gfg')}}" IN FORM (index.html)
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       print(first_name)
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       print(last_name)
       return "Your name is "+first_name + last_name
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)