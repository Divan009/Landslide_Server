from flask_restful import Resource, reqparse
import csv
from decimal import Decimal

from models.landSlide import LandSlideModel

class load(Resource):
    def get(self):
        csvfile = open('landslide_data.csv', newline='')
        row_list = csv.reader(csvfile,delimiter=',')
        for row in row_list:
            land_slide = LandSlideModel(row[0],row[1],row[2],Decimal(row[3]),Decimal(row[4]))
            land_slide.save_to_db()

class all_landslide(Resource):
    def get(self):
        return {'landslides': list(map(lambda x: x.json(), LandSlideModel.query.all()))}
