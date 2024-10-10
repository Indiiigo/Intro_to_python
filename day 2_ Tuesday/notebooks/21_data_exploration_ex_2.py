# ####### step 2
bachelors = adult_df[adult_df["education"] == "Bachelors"]

print("####### step 3")
print("Number of persons with a Bachelor degree as their highest degree:", len(bachelors))

print("####### step 4")
print("Sum of their capital_gain: ", bachelors.capital_gain.sum())

print("####### step 5")
print(bachelors.sex.value_counts())
print('-------OR-------')
print("Female: ", len(bachelors[bachelors["sex"] == "Female"]))
print("Male: ", len(bachelors[bachelors["sex"] == "Male"]))

# ####### step 6
bachelors = bachelors.sort_values(["capital_gain", "age"], ascending=False)

print("####### step 7")
bachelors[(bachelors["age"] >= 20) & (bachelors["age"] <= 40)].head(10)