# TODO: LEARN DATABASE CONNECTION FROM FLASK_SQLALCHEMY DOCUMENTATION
"""
    $ pip install -U Flask-SQLAlchemy
"""
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
#
# class Base(DeclarativeBase):
#     pass
#
# db = SQLAlchemy(model_class=Base)


# TODO: THIS IS FROM SQLALCHEMY DOCS ... USE ABOVE FROM FLASK_SQLALCHEMY DOCS ... EASIER TO USE IN FLASK APP
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy import create_engine, Table, Column, Integer, String, CHAR, MetaData
#
# Base = declarative_base()
# meta_data = MetaData()
#
# test_table = Table(
#     "test_table",
#     meta_data,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(10), nullable=False),
#     Column("gender", CHAR, nullable=False),
#     Column("age", Integer, nullable=False)
# )
#
# print(test_table)
#
# engine = create_engine("sqlite:///test.db")
#
# Session = sessionmaker(engine)
# session = Session()


# TODO: Create Connection to a Database

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

"""
    every FLASK app must have a engine
"""
engine = create_engine("sqlite:///user.db", echo=True)


# TODO: Setting up table info with metadata
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
meta_data = MetaData()

user_table = Table(
    "users",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("name", String(15), nullable=False)
)


"""
    The messages_table holds the ForeignKey
        - this makes a 1 to many relationship between users and messages
"""
messages_table = Table(
    "messages",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("message", String(200), nullable=False)
)

"""
    meta_data.create_all(engine) = This will create the tables made above
"""
# meta_data.create_all(engine)

"""
    meta_data.drop_all(engine) = This will drop all tables in database
"""
# meta_data.drop_all(engine)


#TODO: SHOWS WHERE I LEFT OFF IN SQLAlchemy Documentation
"""
    LAST LEFT OFF = Using ORM Declarative Forms to Define Table Metadata
    LOCATION = Working with Database Metadata
"""
