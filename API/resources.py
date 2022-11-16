from flask_restful import Api, Resource, reqparse
from models import *
api = Api()

parser = reqparse.RequestParser()
parser.add_argument("category_name", type=str)  # declaration of the arguement
parser.add_argument("category_id", type=str)  # declaration of the arguement


class API_R(Resource):
    def get(self):
        cat_jason = {}
        all_cat = Category.query.all()
        for cat in all_cat:
            cat_jason[cat.cat_id] = cat.cat_name

        return cat_jason


class API_UD(Resource):
    # it provides http get,post,put,delete,head as methods.
    def get(self, cat_id):  # it is method of class so we hav to give self
        cat_id_jason = {}
        cat_items = []
        this_cat = Category.query.get(cat_id)
        cat_id_jason["cat_id"] = this_cat.cat_id
        cat_id_jason["cat_name"] = this_cat.cat_name

        for item in this_cat.items:
            cat_items.append(item.item_name)

        cat_id_jason["items"] = cat_items
        return cat_id_jason

    def put(self, cat_id):
        args = parser.parse_args()  # this is where we parse the arguement
        # args = {"category_name": "Chocolate"; "category_id"}
        this_cat = Category.query.get(cat_id)
        this_cat.cat_name = args["category_name"]
        db.session.commit()
        return "", 201


api.add_resource(API_R, "/all_categories")  # convention v2/api/
api.add_resource(API_UD, "/update_category/<int:cat_id>")
