from flask_restful import Resource
from flask import request
import json
# from utils import JSONEncoder
from repositories.vehicle import VehicleRepository
from utils.response import success_response, failure_response



class VehicleResourceByStatus(Resource):
    @staticmethod
    def get():
        try:
            if 'status' in request.args and request.args.get('status') != '' :
                status = request.args.get('status')
                vehicle_status_list = VehicleRepository.get_vehicle_by_status(status)
                return success_response(message="Successfully fetched", content=json.loads(json.dumps(vehicle_status_list, cls=json.JSONEncoder)))
            return failure_response(message="Status not provided")
        except Exception as err:
            return failure_response(str(err))
