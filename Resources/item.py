from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from Models.items import ItemsModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                       type=float,
                       required=True,
                       help="Price can not be empty"
                       )

    parser.add_argument('store_id',
                       type=int,
                       required=True,
                       help="Every Item needs a store id"
                       )


    @jwt_required()
    def get(self,name):
        item =ItemsModel.find_by_name(name)
        if item:
            return item.json()
        return  {'message':'Item does not exist.'}, 404

    def post(self,name):
        if ItemsModel.find_by_name(name):
            return {'message': "An item with name {} already exists".format(name)}, 400
        request_data = Item.parser.parse_args()
        store_item = ItemsModel(name, **request_data)
        try:
            store_item.save_to_db()
        except:
            return {"message" : "An error occured. Please try again."}, 500 #internal server error.
        return store_item.json()

    def delete(self,name):
        item = ItemsModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'{} deleted successfully.'.format(name)}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # del_query = "DELETE FROM items WHERE name=?"
        # cursor.execute(del_query,(name,))
        #
        # connection.commit()
        # connection.close()
        # return {'message': '{} has been deleted successfully.'.format(name)}

    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemsModel.find_by_name(name)
        # updated_item = ItemsModel(name, data['price'])

        if item is None:
            item = ItemsModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemsModel.query.all()]}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # get_query = "SELECT * FROM items"
        # result= cursor.execute(get_query)
        # items = []
        # for row in result:
        #     items.append({'name':row[1],'price':row[2]})
        # connection.close()
        #
        # return {'items':items}