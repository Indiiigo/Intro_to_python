print("A.1 Show for each combination of sex and race, how many instances(people) are contained in the dataset")


df.groupby(["sex", "race"]).size().unstack()