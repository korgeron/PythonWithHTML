"""
    Purpose of this File = To test current knowledge of SQLAlchemy

        - set up a simple database connection
        - store a value into the database
        - display database data to the terminal
"""

from sqlalchemy.orm import DeclarativeBase, mapped_column, Session
from sqlalchemy import create_engine, Integer, String, select

sqlite_engine = create_engine("sqlite:///knowledge.db")


class DBase(DeclarativeBase):
    pass


class CoolTableClub(DBase):
    __tablename__ = "cool_table"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(30), nullable=False)


DBase.metadata.create_all(sqlite_engine)

cool_kid_creation = CoolTableClub(id=None, name="Michael Naaze")

with Session(sqlite_engine) as session:
    session.add(cool_kid_creation)
    session.commit()

with Session(sqlite_engine) as session:
    cool_kid = session.execute(select(CoolTableClub))
    [print(kid[0].name) for kid in cool_kid]

DBase.metadata.drop_all(sqlite_engine)
