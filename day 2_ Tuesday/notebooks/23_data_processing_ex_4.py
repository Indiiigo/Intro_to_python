print("A.3 Show for each combination of marital-Status and race how many males/females over 40 years have a bachelor degree as their highest degree?")


df2 = df[(df["age"] > 40) & (df["education"] =="Bachelors")]
df2.groupby(["marital-status","race","sex"]).size().unstack().fillna(0)
