import pandas as pd

df = pd.read_excel("tuesday_data.xlsx")
# print(df)

df = df.drop(columns=["Unnamed: 0", "Till ID"])
df = df.dropna(how="any")

# print(df)

# print(df["Basket"].value_counts())


# df.info()

# print(df.describe())
# print(df["Transaction Type"].value_counts())
# df = df.drop([0]) 
# df = df.set_index("Transaction ID")

# df.index = df.index.rename("Sale ID")


# print(df)

df = df.drop_duplicates()
# print(df["Transaction Type"].value_counts())


# The total income
# total_income = df["Cost"].sum()
# print(df["Cost"].sum())

#Total income by staff 
# total_income_each_day = df.groupby('Staff')['Cost'].sum()
# print(total_income_each_day)

    
#The worst selling item   
# print(df['Cost'].min())

#The highest spend
# print(df["Cost"].max())

# Explode basket
def remove_punctuation(basket):
    basket = str(basket)
    basket = basket.replace("[", "")
    basket = basket.replace("]", "")
    basket = basket.replace("'", "")
    return basket

# def split_basket(basket_str):
#     elements = basket_str.split(',')
#     stripped_elements = [e.strip() for e in elements]
#     return stripped_elements

df["Basket"] = df["Basket"].apply(remove_punctuation)

def split_baskets(basket_str):
    elements = basket_str.split(',')
    stripped_elements = [e.strip() for e in elements]
    return stripped_elements


df["Basket"] = df["Basket"].apply(split_baskets)
# print(df["Basket"])



# # print(df)


# The total income
total_income = df["Cost"].sum()
print(df["Cost"].sum())

# Total income by staff 
total_income_each_day = df.groupby('Staff')['Cost'].sum()
print(total_income_each_day)

#The worst selling item   
print(df['Cost'].min())

# The highest spend
print(df["Cost"].max())

# # The MVP Staff member
print(df.groupby('Staff')['Cost'].sum().idxmax())

# #The Best-selling item
# print(df["Basket"].mode())
# print(df["Basket"].value_counts())

# #The average basket spend
print(df['Cost'].mean())

df = df.explode("Basket", ignore_index=False)
print(df["Basket"].value_counts())

# #The Best-selling item
print(df["Basket"].mode())
# print(df["Basket"].value_counts())
# print(df)

# print(df.describe())

df.to_excel('result_data.xlsx', index=False)

