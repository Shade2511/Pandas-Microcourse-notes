import pandas as pd

# --- Basic DataFrame creation ---
df = pd.DataFrame({
    'name': ["Jack", "Shade"],
    'ID': ["2511", "1196"]
}, index=["master1", "master2"])  # custom index

# --- Series creation ---
se = pd.Series([1, 2, 3, 4, 5], name="numbers", index=["1-", "2-", "3-", "4-", "5-"])
test = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# --- Accessing data with iloc and loc ---
df2 = pd.DataFrame({
    'name': ["Jack", "Shade", "Man"],
    'Desc': ["i am better", "i am shade", "baba boi"],
    'ID': ["2511", "1196", "001"]
}, index=[1, 2, 3])

# iloc -> access by row position, loc -> access by index label
print(df2.iloc[:2])  # first 2 rows
print(df2.loc[1, "name"])  # specific cell
print(df2.loc[df2.name == "Shade"])  # conditional selection

# --- Handling missing values ---
df3 = pd.DataFrame({
    'name': ["Jack", "Shade", "Man", "Boy"],
    'Desc': ["i am better", "i am shade", "i like candy", None],
    'ID': ["2511", "1196", "001", None]  # None represents missing data
}, index=[1, 2, 3, 4])

print(df3.Desc.isnull())   # check missing values
print(df3.Desc.notnull())  # check non-missing values

# --- Adding new columns dynamically ---
df3["Gender"] = "Unknown"              # same value for all rows
df3["Rank"] = range(len(df3), 0, -1)   # sequential numbers in reverse
df3["Order"] = range(1, len(df3)+1)    # sequential numbers (1..n)
print(df3)

# --- Applying functions on rows/columns ---
dataframe1 = pd.DataFrame({
    "product": ["Ball", "Bat", "Sword", "Gun", "Ball"],
    "price": [20, 50, 120, 500, 20]
}, index=[1, 2, 3, 4, 5])

dataframe1["Dealer"] = range(1, len(dataframe1)+1)

# Using map() to transform column values
avg_price = dataframe1["price"].mean()
dataframe1["price_plus_avg"] = dataframe1["price"].map(lambda p: p + avg_price)

# Custom apply() for row-wise transformation
def discount(row):
    if row["product"] == "Sword":
        row["price"] += 1000
    else:
        row["price"] -= 10
    return row

print(dataframe1.apply(discount, axis="columns"))

# --- Basic DataFrame exploration ---
print(dataframe1.head(1))  # first row
print(dataframe1["product"] + " - " + dataframe1["price"].astype(str))  # combine columns as string

# --- Grouping and Sorting ---
print(dataframe1.groupby("price")["price"].count())        # count per price
print(dataframe1.groupby("price")["price"].min())          # min price per group
print(dataframe1.groupby("product").apply(lambda x: x["product"].iloc[0]))
print(dataframe1.groupby("price")["price"].agg(max))       # max price per group
print(dataframe1.groupby(["price", "product"])["price"].agg(len))  # multi-index

# Index operations
mi = dataframe1.index
print(type(mi))  # Index object
print(dataframe1.sort_values(by=["price","Dealer"], ascending=False))  # multi-sort
print(dataframe1.sort_index())  # sort by index

# --- Data Cleaning & Transformation ---
dataframe1["price"] = dataframe1["price"].astype("float64")  # change column type
print(dataframe1.dtypes)

dataframe1["price"].fillna("Unknown", inplace=True)  # replace missing values
dataframe1["product"].replace("Ball", "Tennis Ball", inplace=True)  # replace value
dataframe1.rename(columns={"product": "Item"}, inplace=True)  # rename column
dataframe1.rename(index={0: 'firstEntry', 1: 'secondEntry'}, inplace=True)  # rename index
print(dataframe1)

# --- Combining DataFrames ---
# Example: join using your dataframe1 (simulate another dealer prices)
other_dealer = pd.DataFrame({
    "Item": ["Bat", "Sword", "Gun", "Tennis Ball"],
    "Dealer": [1, 2, 3, 4],
    "price": [55, 1100, 480, 25]
}).set_index(["Item", "Dealer"])

# join with original dataframe1
combined = dataframe1.set_index(["Item", "Dealer"]).join(other_dealer, lsuffix="_orig", rsuffix="_other")
print(combined)
