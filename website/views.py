from flask import Blueprint, redirect, render_template, url_for, request
from .models import Megabytes
from . import db
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("Agg")

my_view = Blueprint("my_view", __name__)

id_to_day = {
    "Monday": "Monday",
    "Tuesday": "Tuesday",
    "Wednesday": "Wednesday",
    "Thursday": "Thursday",
    "Friday": "Friday",
    "Saturday": "Saturday",
    "Sunday": "Sunday",
}
@my_view.route('/')
def home():
    week_data = Megabytes.query.all()
    if week_data:
        day_income =[]
        week_day = []
        for day in week_data:
            day_income.append(float(day.total_income))
            week_day.append(id_to_day.get(day.day_id))
        print(day.total_income, day_income)
        plt.plot(week_day, day_income, marker = 'o')
        plt.title("Megabytes Income by Week Day", fontsize=15)
        plt.xlabel("Days of The Week", fontsize=14)
        plt.xticks(fontsize = 12) 
        plt.ylabel("Daily Income", fontsize=14)
        plt.yticks(fontsize = 12) 
        plt.savefig("website/static/images/week_income.png")
    return render_template("index.html", week_data = week_data)

@my_view.route('/submit', methods=['POST'])
def submit():
    day_id = request.form.get('day_id').capitalize()
    total_income = request.form.get('total_income').capitalize()
    highest_spend = request.form.get('highest_spend').capitalize()
    best_selling_item = request.form.get('best_selling_item').capitalize()
    worst_selling_item = request.form.get('worst_selling_item').capitalize()
    avg_basket_spend = request.form.get('avg_basket_spend').capitalize()
    staff_mvp = request.form.get('staff_mvp').capitalize()
    new_record = Megabytes(day_id=day_id, total_income=total_income, highest_spend=highest_spend, best_selling_item=best_selling_item, worst_selling_item=worst_selling_item, avg_basket_spend=avg_basket_spend, staff_mvp=staff_mvp)
    db.session.add(new_record)
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/edit_total_income/<data_id>", methods=["POST"])
def edit_total_income(data_id):
    data = Megabytes.query.filter_by(id=data_id).first()
    edit_total_income = request.form.get("edit_total_income")
    data.total_income = edit_total_income
    db.session.commit()
    edition = "Your data was successfully edited!"
    return redirect(url_for("my_view.home", edition=edition))

@my_view.route("/edit_highest_spend/<data_id>", methods=["POST"])
def edit_highest_spend(data_id):
    data = Megabytes.query.filter_by(id=data_id).first()
    edit_highest_spend = request.form.get('edit_highest_spend')
    data.highest_spend = edit_highest_spend
    db.session.commit()
    edition = "Your data was successfully edited!"
    return redirect(url_for("my_view.home", edition=edition))

@my_view.route("/edit_best_selling_item/<data_id>", methods=["POST"])
def edit_best_selling_item(data_id):
    data = Megabytes.query.filter_by(id=data_id).first()
    edit_best_selling_item = request.form.get('edit_best_selling_item')
    data.best_selling_item = edit_best_selling_item
    db.session.commit()
    edition = "Your data was successfully edited!"
    return redirect(url_for("my_view.home", edition=edition))

@my_view.route("/edit_worst_selling_item/<data_id>", methods=["POST"])
def edit_worst_selling_item(data_id):
    data = Megabytes.query.filter_by(id=data_id).first()
    edit_worst_selling_item = request.form.get('edit_worst_selling_item')
    data.worst_selling_item = edit_worst_selling_item
    db.session.commit()
    edition = "Your data was successfully edited!"
    return redirect(url_for("my_view.home", edition=edition))

@my_view.route("/edit_avg_basket_spend/<data_id>", methods=["POST"])
def edit_avg_basket_spend(data_id):
    data = Megabytes.query.filter_by(id=data_id).first()
    edit_avg_basket_spend = request.form.get('edit_avg_basket_spend')
    data.avg_basket_spend = edit_avg_basket_spend
    db.session.commit()
    edition = "Your data was successfully edited!"
    return redirect(url_for("my_view.home", edition=edition))

@my_view.route("/edit_staff_mvp/<data_id>", methods=["POST"])
def edit_staff_mvp(data_id):
    data = Megabytes.query.filter_by(id=data_id).first()
    edit_staff_mvp = request.form.get('edit_staff_mvp')
    data.staff_mvp = edit_staff_mvp
    db.session.commit()
    edition = "Your data was successfully edited!"
    return redirect(url_for("my_view.home", edition=edition))


@my_view.route("/monday/", methods = ['GET', 'POST'])
def monday():
    try:
        week_dat_mon = Megabytes.query.all()
        if week_dat_mon:
            day_income =[]
            day_high_spend = []
            day_best_sell = []
            day_worst_sell = []
            day_avg_basket_cost = []
            day_staff_mvp = []
            week_day = []
            for day in week_dat_mon:
                day_income.append(day.total_income)
                day_high_spend.append(day.highest_spend)
                day_best_sell.append(day.best_selling_item)
                day_worst_sell.append(day.worst_selling_item)
                day_avg_basket_cost.append(day.avg_basket_spend)
                day_staff_mvp.append(day.staff_mvp)
                week_day.append(id_to_day.get(day.day_id))
            monday = week_day[0]
            income = day_income[0]
            spend = day_high_spend[0]
            best_sell = day_best_sell[0]
            worst_sell = day_worst_sell[0]
            basket = day_avg_basket_cost[0]
            staff = day_staff_mvp[0]
        else:
            monday = "No Data Yet"
            income = "No Data Yet"
            spend = "No Data Yet"
            best_sell = "No Data Yet"
            worst_sell = "No Data Yet"
            basket = "No Data Yet"
            staff = "No Data Yet"
    except:
        monday = "No Data Yet"
        income = "No Data Yet"
        spend = "No Data Yet"
        best_sell = "No Data Yet"
        worst_sell = "No Data Yet"
        basket = "No Data Yet"
        staff = "No Data Yet"
    return render_template("monday.html", week_dat_mon=week_dat_mon, monday=monday, income=income, spend=spend, best_sell=best_sell, worst_sell=worst_sell, basket=basket, staff=staff)

@my_view.route("/tuesday/", methods = ['GET', 'POST'])
def tuesday():
    try:
        week_dat_tues = Megabytes.query.all()
        if week_dat_tues:
            day_income =[]
            day_high_spend = []
            day_best_sell = []
            day_worst_sell = []
            day_avg_basket_cost = []
            day_staff_mvp = []
            week_day = []
            for day in week_dat_tues:
                day_income.append(day.total_income)
                day_high_spend.append(day.highest_spend)
                day_best_sell.append(day.best_selling_item)
                day_worst_sell.append(day.worst_selling_item)
                day_avg_basket_cost.append(day.avg_basket_spend)
                day_staff_mvp.append(day.staff_mvp)
                week_day.append(id_to_day.get(day.day_id))
            tuesday = week_day[1]
            income = day_income[1]
            spend = day_high_spend[1]
            best_sell = day_best_sell[1]
            worst_sell = day_worst_sell[1]
            basket = day_avg_basket_cost[1]
            staff = day_staff_mvp[1]
        else:
            tuesday = "No Data Yet"
            income = "No Data Yet"
            spend = "No Data Yet"
            best_sell = "No Data Yet"
            worst_sell = "No Data Yet"
            basket = "No Data Yet"
            staff = "No Data Yet"
    except:
        tuesday = "No Data Yet"
        income = "No Data Yet"
        spend = "No Data Yet"
        best_sell = "No Data Yet"
        worst_sell = "No Data Yet"
        basket = "No Data Yet"
        staff = "No Data Yet"
    return render_template("tuesday.html", week_dat_tues=week_dat_tues, tuesday=tuesday, income=income, spend=spend, best_sell=best_sell, worst_sell=worst_sell, basket=basket, staff=staff)

@my_view.route("/wednesday/", methods = ['GET', 'POST'])
def wednesday():
    try:
        week_dat_wed = Megabytes.query.all()
        if week_dat_wed:
            day_income =[]
            day_high_spend = []
            day_best_sell = []
            day_worst_sell = []
            day_avg_basket_cost = []
            day_staff_mvp = []
            week_day = []
            for day in week_dat_wed:
                day_income.append(day.total_income)
                day_high_spend.append(day.highest_spend)
                day_best_sell.append(day.best_selling_item)
                day_worst_sell.append(day.worst_selling_item)
                day_avg_basket_cost.append(day.avg_basket_spend)
                day_staff_mvp.append(day.staff_mvp)
                week_day.append(id_to_day.get(day.day_id))
            wednesday = week_day[2]
            income = day_income[2]
            spend = day_high_spend[2]
            best_sell = day_best_sell[2]
            worst_sell = day_worst_sell[2]
            basket = day_avg_basket_cost[2]
            staff = day_staff_mvp[2]
        else:
            wednesday = "No Data Yet"
            income = "No Data Yet"
            spend = "No Data Yet"
            best_sell = "No Data Yet"
            worst_sell = "No Data Yet"
            basket = "No Data Yet"
            staff = "No Data Yet"
    except:
        wednesday = "No Data Yet"
        income = "No Data Yet"
        spend = "No Data Yet"
        best_sell = "No Data Yet"
        worst_sell = "No Data Yet"
        basket = "No Data Yet"
        staff = "No Data Yet"
    return render_template("wednesday.html", week_dat_wed=week_dat_wed, wednesday=wednesday, income=income, spend=spend, best_sell=best_sell, worst_sell=worst_sell, basket=basket, staff=staff)

@my_view.route("/thursday/", methods = ['GET', 'POST'])
def thursday():
    try:
        week_dat_thurs = Megabytes.query.all()
        if week_dat_thurs:
            day_income =[]
            day_high_spend = []
            day_best_sell = []
            day_worst_sell = []
            day_avg_basket_cost = []
            day_staff_mvp = []
            week_day = []
            for day in week_dat_thurs:
                day_income.append(day.total_income)
                day_high_spend.append(day.highest_spend)
                day_best_sell.append(day.best_selling_item)
                day_worst_sell.append(day.worst_selling_item)
                day_avg_basket_cost.append(day.avg_basket_spend)
                day_staff_mvp.append(day.staff_mvp)
                week_day.append(id_to_day.get(day.day_id))
            thursday = week_day[3]
            income = day_income[3]
            spend = day_high_spend[3]
            best_sell = day_best_sell[3]
            worst_sell = day_worst_sell[3]
            basket = day_avg_basket_cost[3]
            staff = day_staff_mvp[3]
        else:
            thursday = "No Data Yet"
            income = "No Data Yet"
            spend = "No Data Yet"
            best_sell = "No Data Yet"
            worst_sell = "No Data Yet"
            basket = "No Data Yet"
            staff = "No Data Yet"
    except:
        thursday = "No Data Yet"
        income = "No Data Yet"
        spend = "No Data Yet"
        best_sell = "No Data Yet"
        worst_sell = "No Data Yet"
        basket = "No Data Yet"
        staff = "No Data Yet"
    return render_template("thursday.html", week_dat_thurs=week_dat_thurs, thursday=thursday, income=income, spend=spend, best_sell=best_sell, worst_sell=worst_sell, basket=basket, staff=staff)

@my_view.route("/friday/", methods = ['GET', 'POST'])
def friday():
    try:
        week_dat_fri = Megabytes.query.all()
        if week_dat_fri:
            day_income =[]
            day_high_spend = []
            day_best_sell = []
            day_worst_sell = []
            day_avg_basket_cost = []
            day_staff_mvp = []
            week_day = []
            for day in week_dat_fri:
                day_income.append(day.total_income)
                day_high_spend.append(day.highest_spend)
                day_best_sell.append(day.best_selling_item)
                day_worst_sell.append(day.worst_selling_item)
                day_avg_basket_cost.append(day.avg_basket_spend)
                day_staff_mvp.append(day.staff_mvp)
                week_day.append(id_to_day.get(day.day_id))
            friday = week_day[4]
            income = day_income[4]
            spend = day_high_spend[4]
            best_sell = day_best_sell[4]
            worst_sell = day_worst_sell[4]
            basket = day_avg_basket_cost[4]
            staff = day_staff_mvp[4]
        else:
            friday = "No Data Yet"
            income = "No Data Yet"
            spend = "No Data Yet"
            best_sell = "No Data Yet"
            worst_sell = "No Data Yet"
            basket = "No Data Yet"
            staff = "No Data Yet"
    except:
        friday = "No Data Yet"
        income = "No Data Yet"
        spend = "No Data Yet"
        best_sell = "No Data Yet"
        worst_sell = "No Data Yet"
        basket = "No Data Yet"
        staff = "No Data Yet"
    return render_template("friday.html", week_dat_fri=week_dat_fri, friday=friday, income=income, spend=spend, best_sell=best_sell, worst_sell=worst_sell, basket=basket, staff=staff)

@my_view.route("/saturday/", methods = ['GET', 'POST'])
def saturday():
    try:
        week_dat_sat = Megabytes.query.all()
        if week_dat_sat:
            day_income =[]
            day_high_spend = []
            day_best_sell = []
            day_worst_sell = []
            day_avg_basket_cost = []
            day_staff_mvp = []
            week_day = []
            for day in week_dat_sat:
                day_income.append(day.total_income)
                day_high_spend.append(day.highest_spend)
                day_best_sell.append(day.best_selling_item)
                day_worst_sell.append(day.worst_selling_item)
                day_avg_basket_cost.append(day.avg_basket_spend)
                day_staff_mvp.append(day.staff_mvp)
                week_day.append(id_to_day.get(day.day_id))
            saturday = week_day[5]
            income = day_income[5]
            spend = day_high_spend[5]
            best_sell = day_best_sell[5]
            worst_sell = day_worst_sell[5]
            basket = day_avg_basket_cost[5]
            staff = day_staff_mvp[5]
        else:
            saturday = "No Data Yet"
            income = "No Data Yet"
            spend = "No Data Yet"
            best_sell = "No Data Yet"
            worst_sell = "No Data Yet"
            basket = "No Data Yet"
            staff = "No Data Yet"
    except:
        saturday = "No Data Yet"
        income = "No Data Yet"
        spend = "No Data Yet"
        best_sell = "No Data Yet"
        worst_sell = "No Data Yet"
        basket = "No Data Yet"
        staff = "No Data Yet"
    return render_template("saturday.html", week_dat_sat=week_dat_sat, saturday=saturday, income=income, spend=spend, best_sell=best_sell, worst_sell=worst_sell, basket=basket, staff=staff)

@my_view.route("/sunday/", methods = ['GET', 'POST'])
def sunday():
    try:
        week_dat_sun = Megabytes.query.all()
        if week_dat_sun:
            day_income =[]
            day_high_spend = []
            day_best_sell = []
            day_worst_sell = []
            day_avg_basket_cost = []
            day_staff_mvp = []
            week_day = []
            for day in week_dat_sun:
                day_income.append(day.total_income)
                day_high_spend.append(day.highest_spend)
                day_best_sell.append(day.best_selling_item)
                day_worst_sell.append(day.worst_selling_item)
                day_avg_basket_cost.append(day.avg_basket_spend)
                day_staff_mvp.append(day.staff_mvp)
                week_day.append(id_to_day.get(day.day_id))
            sunday = week_day[6]
            income = day_income[6]
            spend = day_high_spend[6]
            best_sell = day_best_sell[6]
            worst_sell = day_worst_sell[6]
            basket = day_avg_basket_cost[6]
            staff = day_staff_mvp[6]
        else:
            sunday = "No Data Yet"
            income = "No Data Yet"
            spend = "No Data Yet"
            best_sell = "No Data Yet"
            worst_sell = "No Data Yet"
            basket = "No Data Yet"
            staff = "No Data Yet"
    except:
        sunday = "No Data Yet"
        income = "No Data Yet"
        spend = "No Data Yet"
        best_sell = "No Data Yet"
        worst_sell = "No Data Yet"
        basket = "No Data Yet"
        staff = "No Data Yet"
    return render_template("sunday.html", week_dat_sun=week_dat_sun, sunday=sunday, income=income, spend=spend, best_sell=best_sell, worst_sell=worst_sell, basket=basket, staff=staff)

