from modules.db.mongo.models.rides import Rides
from bson import ObjectId
from datetime import datetime


class RidesRepository:
    @staticmethod
    def get_rides_by_status(status):
        try:
            query = [
    {
        '$match': {
            'status': status,
        }
    }
]
            rides = Rides.objects.aggregate(query)
            return list(rides)
        except Exception as err:
            return str(err)