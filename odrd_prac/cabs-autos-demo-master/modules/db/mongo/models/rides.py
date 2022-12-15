from ..connector import db
from .base import BaseModel
from datetime import datetime


class Rides(BaseModel):
    pass
    # trip_id = db.StringField()
    # cab = db.DictField()
    # dates = db.DictField()
    # driver = db.DictField()
    # driver_fcm = db.StringField()
    # from1 = db.DictField(alias="from")
    # journey = db.DictField()
    # otp = db.StringField()
    # payment = db.DictField()
    # rejected_by = db.ListField()
    # review = db.DictField()
    # rider = db.DictField()
    # rider_fcm = db.StringField()
    # status = db.StringField()
    # to = db.DictField()
    # fleet_engine_state = db.StringField()
