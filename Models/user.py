import sqlite3

from db import db

class UserModel(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
        # connection= sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username = ?"   #this sets the query for the database
        # result = cursor.execute(query, (username,))   #this assign the result of the query
        # row = result.fetchone()  #this assign the fetches into the obj row
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
        # connection =sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (id,))
        # row = result.fetchone()
        # if row:
        #     user_id = cls(*row)
        # else:
        #     user_id = None
        #
        # connection.close()
        # return user_id