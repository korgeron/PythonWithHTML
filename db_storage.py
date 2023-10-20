from flask import Flask, render_template, redirect, request
from sqlalchemy import create_engine, select, Integer, String, delete, update
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column

engine = create_engine("sqlite:///chat.db", echo=True)


class Base(DeclarativeBase):
    pass


class Messages(Base):
    __tablename__ = "messages"
    id = mapped_column(Integer, primary_key=True)
    message = mapped_column(String(200), nullable=False)


Base.metadata.create_all(engine)

app = Flask("__name__")


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        message_text = request.form["user_input"]
        message_to_store = Messages(id=None, message=message_text)
        with Session(engine) as session:
            session.add(message_to_store)
            session.commit()
        return redirect("/")

    with Session(engine) as session:
        messages = session.scalars(select(Messages))
        return render_template("db_storage.html", messages=messages)


@app.route("/delete/<ID>")
def delete_message(ID):
    clear_message = delete(Messages).where(Messages.id == ID)
    with Session(engine) as session:
        session.execute(clear_message)
        session.commit()
    return redirect("/")


@app.route("/update/<ID>")
def update_message_landing_page(ID):
    print(ID)
    with Session(engine) as session:
        message_to_update = session.execute(select(Messages).where(Messages.id == ID))
        return render_template("update_message.html", update=message_to_update)


@app.route("/update_message", methods=["POST", "GET"])
def message_updated():
    if request.method == "POST":
        new_message = request.form["message"]
        message_id = request.form["message_id"]
        with Session(engine) as session:
            session.execute(update(Messages).where(Messages.id == message_id).values(message=new_message))
            session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
