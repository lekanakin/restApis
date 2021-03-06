
from flask_restful import Resource
from Models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        return {'message': '{} does not exist on the database'.format(name)}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': '{} already exists'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred'}, 500

        return store.json(),201

    def delete(self,name):
        store = StoreModel(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {'message': '{} does not exist on the database'.format(name)}
        return {'message':'Store Deleted.'}


class StoreList(Resource):
    def get(self):
        return {'store': [store.json() for store in StoreModel.query.all()]}
