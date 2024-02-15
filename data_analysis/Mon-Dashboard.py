from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def read_excel_data(filename):
    df = pd.read_excel(filename)
    return df

def extract_items(data):
    
    data = data.dropna(subset=['Basket'])
    
    items = data['Basket'].apply(lambda x: eval(x))
    # Flatten the list of items
    items_flat = [item for sublist in items for item in sublist]
    return items_flat

def daily_stats(data):
    total_income = data['Cost'].sum()
    
    highest_spend = data['Cost'].max()
    
    items_sold = extract_items(data)
    
    item_counts = pd.Series(items_sold).value_counts()

    sales_by_staff = data.groupby('Staff')['Cost'].sum()

    best_staff = sales_by_staff.idxmax()

    best_selling_item = item_counts.idxmax()
    
    worst_selling_item = item_counts.idxmin()
    
    average_basket_spend = round(data['Cost'].mean(), 2)
    
    return total_income, highest_spend, best_selling_item, worst_selling_item, average_basket_spend, sales_by_staff, best_staff

@app.route('/')
def display_results():
    data = read_excel_data('monday_data.xlsx')
    total_income, highest_spend, best_selling_item, worst_selling_item, average_basket_spend, sales_by_staff, best_staff = daily_stats(data)
    return render_template('mon-dash.html', total_income=total_income, highest_spend=highest_spend,
                        best_selling_item=best_selling_item, worst_selling_item=worst_selling_item,
                        average_basket_spend=average_basket_spend, sales_by_staff=sales_by_staff, best_staff=best_staff)

if __name__ == '__main__':
    app.run(debug=True)

