import sqlite3
from flask_restful import Resource,reqparse
from Models.user import UserModel

#User register resource
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Username can not be empty"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Password can not be empty"
                        )
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'User with this username already exists'}, 400
        User = UserModel(**data)
        User.save_to_db()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'],data['password']))
        #
        # connection.commit()
        # connection.close()
        return {'message':'User created successfully'}, 201
