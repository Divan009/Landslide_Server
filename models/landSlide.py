from db import db


class LandSlideModel(db.Model):
    __tablename__ = 'LandSlideTable'

    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(80))
    country_code = db.Column(db.String(10))
    admin_division_name = db.Column(db.String(80))
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)


    def __init__(self,country_name,country_code,admin_division_name,latitude,longitude):
        self.country_name = country_name
        self.country_code = country_code
        self.admin_division_name = admin_division_name
        self.latitude = latitude
        self.longitude = longitude


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'id':self.id,
                'country_name':self.country_name,
                'country_code':self.country_code,
                'admin_division_name':self.admin_division_name,
                'latitude':str(self.latitude),
                'longitude':str(self.longitude)}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_country_name(cls, country_name):
        return cls.query.filter_by(country_name=country_name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
