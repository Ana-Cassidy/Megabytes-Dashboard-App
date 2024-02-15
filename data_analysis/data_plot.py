import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel("Megabytes_average_basket.xlsx")

df2 = pd.read_excel("Megabytes_frequency_sold_items.xlsx")
df2_wed = df2.drop(columns=["Basket Items Thurs", "Frequency Thurs", "Basket Items Sat", "Frequency Sat"])
df2_wed = df2_wed.drop([11])
df2_thurs = df2.drop(columns=["Basket Items Wed", "Frequency Wed", "Basket Items Sat", "Frequency Sat"])
df2_sat = df2.drop(columns=["Basket Items Wed", "Frequency Wed", "Basket Items Thurs", "Frequency Thurs"])

df3 = pd.read_excel("Megabytes_highest_spend.xlsx")

df4 = pd.read_excel("Megabytes_Week_Income_Staff.xlsx")
df4_wed = df4.drop(columns=["Income Thurs", "Income Sat"])
df4_thurs = df4.drop(columns=["Income Wed", "Income Sat"])
df4_sat = df4.drop(columns=["Income Wed", "Income Thurs"])
# print(df4_wed)
# print(df4_thurs)
# print(df4_sat)

df5 = pd.read_excel("Megabytes_Frequency_Payment_Method.xlsx")
df5_wed = df5.drop(columns=["Frequency Thurs", "Frequency Sat"])
df5_thurs = df5.drop(columns=["Frequency Wed", "Frequency Sat"])
df5_sat = df5.drop(columns=["Frequency Wed", "Frequency Thurs"])

plt.style.use('ggplot')

# Plot Megabytes_average_basket

# plt.bar("Day", "Average Basket Cost", data = df1)
# plt.title("Average Basket Cost")
# plt.ylabel("Price")
# plt.savefig("average_basket_cost.png", bbox_inches="tight")

#-------------------------------------#
# Plot Megabytes_frequency_sold_items #
#-------------------------------------#

# Wednesday
# plt.barh("Basket Items Wed", "Frequency Wed", data = df2_wed)
# plt.title("Number of items sold on Wednesday")
# plt.xlabel("Total number of items")
# plt.savefig("Number of items sold on Wednesday.png", bbox_inches="tight")

# Thursday
# plt.barh("Basket Items Thurs", "Frequency Thurs", data = df2_thurs)
# plt.title("Number of items sold on Thursday")
# plt.xlabel("Total number of items")
# plt.savefig("Number of items sold on Thursday.png", bbox_inches="tight")

# Saturday
# plt.barh("Basket Items Sat", "Frequency Sat", data = df2_sat)
# plt.title("Number of items sold on Saturday")
# plt.xlabel("Total number of items")
# plt.savefig("Number of items sold on Saturday.png", bbox_inches="tight")

#------------------------------#
# Plot Megabytes_highest_spend #
#------------------------------#

# Week
# plt.bar("Day", "Highest Spend", data = df3)
# plt.title("Week's Highest Spends")
# plt.ylabel("Amount Spend")
# plt.savefig("Week's Highest Spends.png", bbox_inches="tight")

#----------------------------------#
# Plot Megabytes_Week_Income_Staff #
#----------------------------------#

# Wednesday
# plt.barh("Staff", "Income Wed", data = df4_wed)
# plt.title("Income by Staff Member on Wednesday")
# plt.xlabel("Income")
# plt.savefig("Income by Staff Member on Wednesday.png", bbox_inches="tight")

# Thursday
# plt.barh("Staff", "Income Thurs", data = df4_thurs)
# plt.title("Income by Staff Member on Thursday")
# plt.xlabel("Income")
# plt.savefig("Income by Staff Member on Thursday.png", bbox_inches="tight")

# Saturday
# plt.barh("Staff", "Income Sat", data = df4_sat)
# plt.title("Income by Staff Member on Saturday")
# plt.xlabel("Income")
# plt.savefig("Income by Staff Member on Saturday.png", bbox_inches="tight")

#-----------------------------------------#
# Plot Megabytes_Frequency_Payment_Method #
#-----------------------------------------#
#------------#
# Bar Charts #
#------------#

# Wednesday
# plt.barh("Payment Method", "Frequency Wed", data = df5_wed)
# plt.title("Frequency of Payment Methods on Wednesday")
# plt.xlabel("Frequency")
# plt.savefig("Frequency of Payment Methods on Wednesday.png", bbox_inches="tight")

# Thursday
# plt.barh("Payment Method", "Frequency Thurs", data = df5_thurs)
# plt.title("Frequency of Payment Methods on Thursday")
# plt.xlabel("Frequency")
# plt.savefig("Frequency of Payment Methods on Thursday.png", bbox_inches="tight")

# Saturday
# plt.barh("Payment Method", "Frequency Sat", data = df5_sat)
# plt.title("Frequency of Payment Methods on Saturday")
# plt.xlabel("Frequency")
# plt.savefig("Frequency of Payment Methods on Saturday.png", bbox_inches="tight")

#------------#
# Pie Charts #
#------------#

# Wednesday - pie
# freq_wed = df5_wed["Frequency Wed"]
# pay_met_wed = df5_wed["Payment Method"]
# plt.pie(freq_wed, labels = pay_met_wed, autopct="%.1f%%") # , explode=[0.1,0,0,0]
# plt.title("Payment Methods used Wednesday")
# plt.savefig("Payment Methods used Wednesday.png", bbox_inches="tight")

# Thursday - pie
# freq_thurs = df5_thurs["Frequency Thurs"]
# pay_met_thurs = df5_thurs["Payment Method"]
# plt.pie(freq_thurs, labels = pay_met_thurs, autopct="%.1f%%") # , explode=[0.1,0,0,0]
# plt.title("Payment Methods used Thursday")
# plt.savefig("Payment Methods used Thursday.png", bbox_inches="tight")

# Saturday - pie
# freq_sat = df5_sat["Frequency Sat"]
# pay_met_sat = df5_sat["Payment Method"]
# plt.pie(freq_sat, labels = pay_met_sat, autopct="%.1f%%") # , explode=[0.1,0,0,0]
# plt.title("Payment Methods used Saturday")
# plt.savefig("Payment Methods used Saturday.png", bbox_inches="tight")

# plt.show()