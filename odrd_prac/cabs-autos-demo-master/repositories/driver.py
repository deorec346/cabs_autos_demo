from modules.db.mongo.models.rides import Rides


class DriverRepository:
    @staticmethod
    def create(payload):
        driver = Rides(**payload)
        return driver.save(payload) 