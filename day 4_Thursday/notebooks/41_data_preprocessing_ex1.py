print("A Use Census data")


df = pd.read_csv ("data/adult.csv", na_values="?")
df.head()

print("A. Show for each combination of sex and race, how many instances(people) are contained in the dataset")


df.groupby(["sex", "race"]).size().unstack()

print("B. What is the mean age of men and women in this dataset?")


g = df[['sex', 'age']].groupby("sex")
g.mean()["age"]

print("C. Show for each combination of marital-Status and race how many males/females over 40 years have a bachelor degree as their highest degree?")


df2 = df[(df["age"] > 40) & (df["education"] =="Bachelors")]
df2.groupby(["marital-status","race","sex"]).size().unstack().fillna(0)