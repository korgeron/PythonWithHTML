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
# from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
#
# meta_data = MetaData()

# user_table = Table(
#     "users",
#     meta_data,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(15), nullable=False)
# )

"""
    The messages_table holds the ForeignKey
        - this makes a 1 to many relationship between users and messages
"""
# messages_table = Table(
#     "messages",
#     meta_data,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", ForeignKey("users.id"), nullable=False),
#     Column("message", String(200), nullable=False)
# )

"""
    meta_data.create_all(engine) = This will create the tables made above
"""
# meta_data.create_all(engine)

"""
    meta_data.drop_all(engine) = This will drop all tables in database
"""
# meta_data.drop_all(engine)

# TODO: USING A DECLARATIVE BASE TO ESTABLISH TABLES
from sqlalchemy.orm import DeclarativeBase

"""
    To use DeclarativeBase class .. you must create a new class that subclasses
    
        ex. >>> from sqlalchemy.orm import DeclarativeBase
            >>> class Base(DeclarativeBase):
            ...     pass
"""


class Base(DeclarativeBase):
    pass


# TODO: DECLARING MAPPED CLASSES
# from typing import List, Optional
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import String

"""
    We will be using classes to set up Tables in the Database
    This class will take in the Base class declared above
"""

"""
    START OF CREATING USER / ADDING TO DATABASE / SELECTING USER ADDED
"""
# class User(Base):
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     first_name: Mapped[str] = mapped_column(String(15), nullable=False)
#     last_name: Mapped[str] = mapped_column(String(20), nullable=False)


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# tess = User(id=None, first_name="Tess", last_name="Ting")

from sqlalchemy.orm import Session
from sqlalchemy import select

"""
    Below adds the User tess to the User Table
"""
# with Session(engine) as session:
#     session.add(tess)
#     session.commit()

"""
    Below is a select statement based on user first_name
"""
# with Session(engine) as sess:
#     stmt = select(User).filter_by(first_name="Tess")
#     user = sess.scalar(stmt)
#     print(user.first_name)

"""
    Can also be written as:
    
        class User(Base):
            __tablename__ = "users"

            id = mapped_column(Integer, primary_key=True)
            first_name = mapped_column(String(15), nullable=False)
            last_name = mapped_column(String(20), nullable=False)
"""

"""
    END OF CREATING USER / ADDING TO DATABASE / SELECTING USER ADDED
"""

# TODO: CREATE MESSAGE TABLE WITHOUT USING Mapped[]
# from sqlalchemy.orm import Session, mapped_column
# from sqlalchemy import Integer, String, select


# class Messages(Base):
#     __tablename__ = "messages"
#
#     id = mapped_column(Integer, primary_key=True)
#     message = mapped_column(String(200), nullable=False)


# Base.metadata.create_all(engine)

# message = Messages(id=None, message="Hello there! My name is John.")

# with Session(engine) as sess:
#     sess.add(message)
#     sess.commit()


# with Session(engine) as sess:
#     stmt = select(Messages).filter_by(id=1)
#     obj = sess.scalar(stmt)
#     print(obj.message)

# TODO: LETS INSERT SOME DATA INTO THE USERS TABLE
"""
    To do this we must
        1. from sqlalchemy import insert
        2.  stmt = insert(user_table).values()
"""

# TODO: SHOWS WHERE I LEFT OFF IN SQLAlchemy Documentation
"""
    LAST LEFT OFF = Using ORM Declarative Forms to Define Table Metadata
    LOCATION = Working with Database Metadata
"""
