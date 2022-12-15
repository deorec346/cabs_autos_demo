from modules.db.mongo.models.rides import Rides
from bson import ObjectId
from datetime import datetime


class VehicleRepository:
    @staticmethod
    def create(payload):
        vehicle = Rides(**payload)
        return vehicle.save(payload)

    # @staticmethod
    # def get_vehicles_by_id(vehicle_id):

    @staticmethod
    def get_vehicle_by_status(status):
        try:

            query = [
        {
            '$match': {
                'status': status
            }
        },      {
            '$project': {
                'cab': '$cab'
            }
        }
    ]
            vehicles = Rides.objects.aggregate(query)
            return list(vehicles)
        except Exception as err:
            return str(err)