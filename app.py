import os
from flask import Flask,jsonify
from flask_restful import Api

from resources.landSlide import load,all_landslide

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'TEMP_TEST_XXXXX362357_SECRET_KEY'

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#api.add_resource(load,'/load')
api.add_resource(all_landslide,'/all')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0',threaded=True,port=5000, debug=True)
