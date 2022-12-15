from flask_restful import Resource
from flask import request
import json
# from utils import JSONEncoder
from bson import ObjectId
from repositories.rides import RidesRepository
from utils.response import success_response, failure_response



class RidesResourceByStatus(Resource):

    @staticmethod
    def get():
        try:
            if 'status' in request.args and request.args.get('status') != '':
                status = request.args.get('status')
                rides_status_list = RidesRepository.get_rides_by_status(status)
                return success_response(message="Successfully fetched", content=json.loads(json.dumps(rides_status_list, cls=json.JSONEncoder)))
            return failure_response(message="Status not provided")
        except Exception as err:
            return failure_response(str(err))

