from flask import Blueprint,request,abort,make_response
from app.models.caretaker import Caretaker
from .route_utilities import validate_model
from app.models.cat import Cat
from ..db import db

bp = Blueprint("caretakers_bp", __name__, url_prefix="/caretakers")

@bp.post("")
def create_caretaker():
    request_body = request.get_json()

    try:
        new_caretaker = Caretaker.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request:missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_caretaker)
    db.session.commit()

    return new_caretaker.to_dict(),201

@bp.get("")
def get_all_caretakers():
    query = db.select(Caretaker)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Caretaker.name.ilike(f"%{name_param}%"))

    caretakers = db.session.scalars(query.order_by(Caretaker.id))
    caretakers_reponse = [caretaker.to_dict() for caretaker in caretakers]

    return caretakers_reponse

@bp.post("/<caretaker_id>/cats")
def create_cat_with_caretaker_id(caretaker_id):
    caretaker = validate_model(Caretaker,caretaker_id)
    request_body = request.get_json()
    request_body["caretaker_id"] = caretaker.id

    try:
        new_cat= Cat.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request:missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_cat)
    db.session.commit()

    return new_cat.to_dict, 201