import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data_file(filename):
    df = pd.read_excel(filename)
    return df

def data_info():
    data_general_info = show_data_analysis()
    data_general_info.info()
    data_desciption = show_data_analysis()
    data_desciption = data_desciption.describe()
    print(data_desciption)


def show_data_analysis():
    data_analysis = read_data_file("wednesday_data.xlsx")
    return data_analysis

def run_analysis_wednesday():
    data_info()

# wednesday = run_analysis_wednesday()
# print(wednesday)

# df_wednesday = pd.read_excel("wednesday_data.xlsx")
# df4 = pd.read_excel("thursday_data.xlsx")
# df6 = pd.read_excel("saturday_data.xlsx")

# # print(df6)

# # df6.info()
# # print(df6.describe())

# # Wednesday
# df_wednesday = df_wednesday.drop([0])
# df_wednesday = df_wednesday.drop(columns=["Unnamed: 0", "Till ID"])
# df_wednesday = df_wednesday.set_index("Transaction ID")
# df_wednesday = df_wednesday.drop_duplicates()

# # Thursday
# df4 = df4.drop([0])
# df4 = df4.drop(columns=["Unnamed: 0", "Till ID"])
# df4 = df4.set_index("Transaction ID")

# # Saturday
# df6 = df6.drop([0])
# df6 = df6.drop(columns=["Unnamed: 0", "Till ID"])
# df6 = df6.set_index("Transaction ID")

# # print(df6)

# #----------------------------------------#
# # Transaction Type Frequencies (General) #
# #----------------------------------------#

# # Wednesday
# num_trans_by_type = df_wednesday["Transaction Type"].value_counts()
# df3_num_trans_type = num_trans_by_type.reset_index().rename(columns={"count": "Frequency Wed"})

# # Thursday
# num_trans_by_type4 = df4["Transaction Type"].value_counts()
# df4_num_trans_type = num_trans_by_type4.reset_index().rename(columns={"count": "Frequency Thurs"})
# df4_num_trans_type = df4_num_trans_type.drop(columns=["Transaction Type"])

# # Saturday
# num_trans_by_type6 = df6["Transaction Type"].value_counts()
# df6_num_trans_type = num_trans_by_type6.reset_index().rename(columns={"count": "Frequency Sat"})
# df6_num_trans_type = df6_num_trans_type.drop(columns=["Transaction Type"])

# # Week
# df_freq_trans_type_week = pd.concat([df3_num_trans_type, df4_num_trans_type, df6_num_trans_type], axis=1)
# df_freq_trans_type_week.to_excel("Megabytes_Frequency_Transaction_Types.xlsx", index=False)


# #---------------------------------------#
# # Transaction Type Frequencies by Staff #
# #---------------------------------------#

# # Wednesday
# num_trans_type_by_staff = df_wednesday.groupby("Staff")["Transaction Type"].value_counts()
# df3_freq_transtype_staff = num_trans_type_by_staff.reset_index().rename(columns={"Staff": "Staff Wed", "Transaction Type": "Transaction Wed", "count": "Wednesday"})


# # Thursday
# num_trans_type_by_staff4 = df4.groupby("Staff")["Transaction Type"].value_counts()
# df4_freq_transtype_staff = num_trans_type_by_staff4.reset_index().rename(columns={"Staff": "Staff Thurs", "Transaction Type": "Transaction Thurs","count": "Thursday"})
# # df4_freq_transtype_staff = df4_freq_transtype_staff.drop(columns=["Staff", "Transaction Type"])

# # Saturday
# num_trans_type_by_staff6 = df6.groupby("Staff")["Transaction Type"].value_counts()
# df6_freq_transtype_staff = num_trans_type_by_staff6.reset_index().rename(columns={"Staff": "Staff Sat", "Transaction Type": "Transaction Sat","count": "Saturday"})

# # Week
# df_trans_type_staff_week = pd.concat([df3_freq_transtype_staff, df4_freq_transtype_staff, df6_freq_transtype_staff], axis=1)
# # print(df_trans_type_staff_week)
# df_trans_type_staff_week.to_excel("Megabytes_Staff_Transactions.xlsx", index=False)

# #---------------------------------#
# # Further cleaning: drop NaN rows #
# #---------------------------------# 

# # Wednesday
# df_wednesday = df_wednesday.dropna(how="any")
# df_wednesday = df_wednesday.replace("voucher", "Voucher")
# df_wednesday = df_wednesday.replace("debit", "Debit")
# df_wednesday = df_wednesday.replace("cash", "Cash")
# df_wednesday = df_wednesday.replace("credit", "Credit")

# # Thursday
# df4 = df4.dropna(how="any")
# df4 = df4.replace(700, 7)

# # Saturday
# df6 = df6.dropna(how="any")
# # print(df6)

# #-----------------#
# # Payment Methods #
# #-----------------# 

# # Wednesday
# num_pay_method = df_wednesday["Payment Method"].value_counts()
# df3_num_pay_method = num_pay_method.reset_index().rename(columns={"count": "Frequency Wed"})

# # Thursday
# num_pay_method4 = df4["Payment Method"].value_counts()
# df4_num_pay_method = num_pay_method4.reset_index().rename(columns={"count": "Frequency Thurs"})
# df4_num_pay_method = df4_num_pay_method.drop(columns=["Payment Method"])

# # Saturday
# num_pay_method6 = df6["Payment Method"].value_counts()
# df6_num_pay_method = num_pay_method6.reset_index().rename(columns={"count": "Frequency Sat"})
# df6_num_pay_method = df6_num_pay_method.drop(columns=["Payment Method"])

# # Week
# df_pay_method_week = pd.concat([df3_num_pay_method, df4_num_pay_method, df6_num_pay_method], axis=1)
# df_pay_method_week.to_excel("Megabytes_Frequency_Payment_Method.xlsx", index=False)

# #--------------#
# # Total income #
# #--------------#

# # Wednesday
# total_income = df_wednesday["Cost"].sum()

# # Thursday
# total_income4 = df4["Cost"].sum()

# # Saturday
# total_income6 = df6["Cost"].sum()

# # Week
# df_income_week = pd.DataFrame ([("Wednesday", total_income),("Thursday", total_income4),("Saturday", total_income6)], columns=["Day", "Total Income"])
# df_income_week.to_excel("Megabytes_Week_Income.xlsx", index=False)


# #--------------------------#
# #   Total income by staff  #
# #--------------------------#

# # Wednesday

# # Income achieved by each member of staff
# income_by_staff = df_wednesday.groupby("Staff")["Cost"].sum()
# income_by_staff  = income_by_staff.reset_index().rename(columns={"Cost": "Income Wed"})

# # Thursday
# income_by_staff4 = df4.groupby("Staff")["Cost"].sum()
# income_by_staff4 = income_by_staff4.reset_index().rename(columns={"Cost": "Income Thurs"})
# income_by_staff4 = income_by_staff4.drop(columns=["Staff"])

# # Saturday
# income_by_staff6 = df6.groupby("Staff")["Cost"].sum()
# income_by_staff6 = income_by_staff6.reset_index().rename(columns={"Cost": "Income Sat"})
# income_by_staff6 = income_by_staff6.drop(columns=["Staff"])

# # Week
# df_income_staff_week = pd.concat([income_by_staff, income_by_staff4, income_by_staff6], axis=1)
# # df_income_staff_week = df_income_staff_week.transpose()
# # print(df_income_staff_week)
# df_income_staff_week.to_excel("Megabytes_Week_Income_Staff.xlsx", index=False)


# #-------------------#
# # Highest day spend #
# #-------------------#

# # Wednesday
# highest_spend = df_wednesday["Cost"].max()

# # Thursday
# highest_spend4 = df4["Cost"].max()

# # Saturday
# highest_spend6 = df6["Cost"].max()

# # Week
# df_highest_spend_week = pd.DataFrame ([("Wednesday", highest_spend),("Thursday", highest_spend4),("Saturday", highest_spend6)], columns=["Day", "Highest Spend"])
# df_highest_spend_week.to_excel("Megabytes_highest_spend.xlsx", index=False)


# #----------------------#
# # Average basket spent #
# #----------------------#

# # Wednesday
# avg_basket_cost = df_wednesday["Cost"].mean()

# # Thursday
# avg_basket_cost4 = df4["Cost"].mean()

# # Saturday
# avg_basket_cost6 = df6["Cost"].mean()

# df_average_basket_cost = pd.DataFrame ([("Wednesday", avg_basket_cost),("Thursday", avg_basket_cost4),("Saturday", avg_basket_cost6)], columns=["Day", "Average Basket Cost"])
# df_average_basket_cost.to_excel("Megabytes_average_basket.xlsx", index=False)

# #-----------------#
# # Explode baskets #
# #-----------------#

# def remove_punctuation(basket):
#     basket = str(basket)
#     basket = basket.replace("[","")
#     basket = basket.replace("]","")
#     basket = basket.replace("'","")
#     return basket


# def split_basket(basket_str):
#     elements = basket_str.split(",")
#     stripped_elements = [e.strip() for e in elements]
#     return stripped_elements


# # Wednesday
# df_wednesday["Basket"] = df_wednesday["Basket"].apply(remove_punctuation)
# df_wednesday["Basket"] = df_wednesday["Basket"].apply(split_basket)
# df_wednesday = df_wednesday.explode("Basket", ignore_index=False)

# # Thursday
# df4["Basket"] = df4["Basket"].apply(remove_punctuation)
# df4["Basket"] = df4["Basket"].apply(split_basket)
# df4 = df4.explode("Basket", ignore_index=False)

# # Saturday
# df6["Basket"] = df6["Basket"].apply(remove_punctuation)
# df6["Basket"] = df6["Basket"].apply(split_basket)
# df6 = df6.explode("Basket", ignore_index=False)

# #------------------------------#
# # Best and Least selling items #
# #------------------------------#

# # Wednesday
# item_freq = df_wednesday["Basket"].value_counts()
# item_freq = item_freq.reset_index().rename(columns={"Basket":"Basket Items Wed", "count":"Frequency Wed"})
# # item_freq = item_freq.sort_values(by=["Basket Items Wed"])


# #Thursday
# item_freq4 = df4["Basket"].value_counts()
# item_freq4 = item_freq4.reset_index().rename(columns={"Basket":"Basket Items Thurs", "count":"Frequency Thurs"})
# # item_freq4 = item_freq4.sort_values(by=["Basket Items Thurs"])

# #Thursday
# item_freq6 = df6["Basket"].value_counts()
# item_freq6 = item_freq6.reset_index().rename(columns={"Basket":"Basket Items Sat", "count":"Frequency Sat"})

# # Week
# df_freq_items_sold = pd.concat([item_freq, item_freq4, item_freq6], axis=1)
# df_freq_items_sold.to_excel("Megabytes_frequency_sold_items.xlsx", index=False)




# fav_items = df_wednesday["Basket"].mode()
# fav_item = df_wednesday["Basket"].value_counts().idxmax()
# least_popular_item = min(df_wednesday["Basket"].unique(), key=df_wednesday["Basket"].tolist().count)