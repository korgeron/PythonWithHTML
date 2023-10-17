from flask import Flask, render_template, request, url_for, redirect

app = Flask("__name__")


data_base = {}
def get_last_index(db):
    if len(db) != 0:
        copy = db.copy()
        last_instance = copy.popitem()
        return last_instance[0]
    else:
        return -1


@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        user_value = request.form.get("user_value")
        key = get_last_index(data_base) + 1
        print("NEW_INDEX = " + str(key))
        data_base.update({key:user_value})
        return redirect("/")

    return render_template("index.html", tests=data_base)

@app.route("/delete/<id>")
def delete(id):
    print("ID = " + id)
    data_base.pop(int(id))
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
