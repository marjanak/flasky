from flask import Blueprint,abort,make_response,request
# from ..models.cat import cats
from ..db import db
from app.models.cat import Cat

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")


@cats_bp.post("")
def create_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body ["color"]
    personality = request_body ["personality"]


    new_cat = Cat(name=name, color=color, personality=personality)

    db.session.add(new_cat)
    db.session.commit()

    response = new_cat.to_dict()
    return response, 201

@cats_bp.get("")
def get_all_cats():
    query = db.select(Cat).order_by(Cat.id)
    cats = db.session.scalars(query)

    cats_response =[cat.to_dict() for cat in cats]
    return cats_response
