from flask import Blueprint, redirect, render_template, url_for, request
from .models import Megabytes
from . import db
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

my_view = Blueprint("my_view", __name__)

@my_view.route('/')
def home():
    week_data = Megabytes.query.all()
    return render_template("index.html", week_data = week_data)

@my_view.route('/submit', methods=['POST'])
def submit():
    total_income = request.form.get('total_income')
    highest_spend = request.form.get('highest_spend')
    best_selling_item = request.form.get('best_selling_item')
    worst_selling_item = request.form.get('worst_selling_item')
    avg_basket_spend = request.form.get('avg_basket_spend')
    staff_mvp = request.form.get('staff_mvp')

    new_record = Megabytes(total_income=total_income, highest_spend=highest_spend, best_selling_item=best_selling_item, worst_selling_item=worst_selling_item, avg_basket_spend=avg_basket_spend, staff_mvp=staff_mvp)

    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for("my_view.home"))
