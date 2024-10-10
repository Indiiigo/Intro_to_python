print("A.2 What is the mean age of men and women in this dataset?")


g = df.groupby("sex")
g.mean()["age"]

