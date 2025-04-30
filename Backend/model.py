
from setting import db

class Company_list(db.Model):
    __tablename__ = 'company_list'

    id = db.Column(db.Integer, primary_key=True)
    Company_name = db.Column(db.String(100), nullable=False)  # Change column name here
    Status = db.Column(db.String(50))
    Clicks = db.Column(db.Integer)
    Cost = db.Column(db.Integer)
    Impressions = db.Column(db.Integer)
