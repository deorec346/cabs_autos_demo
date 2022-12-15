from flask import Blueprint
from flask_restful import Api
from resources.organization import OrganizationResource, OrganizationResourceById
from resources.rides import RidesResourceByStatus
from resources.vehicle import VehicleResourceByStatus 

ORGANIZATION_BLUEPRINT = Blueprint('Organization', __name__)
Api(ORGANIZATION_BLUEPRINT).add_resource(OrganizationResource, '/onboarding_organization')

ORGANIZATIONS_BLUEPRINT = Blueprint('Organizations', __name__)
Api(ORGANIZATIONS_BLUEPRINT).add_resource(OrganizationResourceById, '/org/<string:id>')

RIDES_BLUEPRINT = Blueprint('Rides', __name__)
Api(RIDES_BLUEPRINT).add_resource(RidesResourceByStatus, '/rides')

VEHICLE_BLUEPRINT = Blueprint('Vehicles', __name__)
Api(VEHICLE_BLUEPRINT).add_resource(VehicleResourceByStatus, '/vehicles')