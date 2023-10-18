import pandas as pd

# ####### step 1
adult_df = pd.read_csv("adult.csv", na_values="?")

# ####### step 2
# get a subset of dataframe
adult_df = adult_df[["age", "sex", "education", "hours-per-week", "capital-gain"]]

# ####### step 3
# rename a column
adult_df.rename(columns={"capital-gain" : "capital_gain"}, inplace=True)

print("####### step 4")
print("Column names:", adult_df.columns.values)

print("####### step 5")
print("Number of different 'education' values:", len(adult_df["education"].unique()))

print("####### step 6")
print("Mean 'working time per week':", adult_df["hours-per-week"].mean())

print("####### step 7")
# adult_df["capital_gain"].max()
print("Max capital gain:", adult_df.capital_gain.max())