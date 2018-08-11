# Import the database object (db) from the main application module
from app import db

class FeatureModel(db.Model):
    __tablename__ = "Features"

    id = db.Column(db.Integer, primary_key=True)    
    client = db.Column(db.String(50), nullable=False)
    product_area = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Feature Title %r>' % self.title