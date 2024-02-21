from . import db
import datetime

class Megabytes(db.Model):
    day_id = db.Column(db.String(300), primary_key = True)
    total_income = db.Column(db.String(300))
    highest_spend = db.Column(db.String(300))
    best_selling_item = db.Column(db.String(300))
    worst_selling_item = db.Column(db.String(300))
    avg_basket_spend = db.Column(db.String(300))
    staff_mvp = db.Column(db.String(300))
