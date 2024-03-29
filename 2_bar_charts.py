import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("fivethirtyeight")

with open("data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    lang_counter = Counter()

    for row in csv_reader:
        lang_counter.update(row["LanguagesWorkedWith"].split(";"))


languages = []
popularity =[]

for lang in lang_counter.most_common(15):
    languages.append(lang[0])
    popularity.append(lang[1])

plt.barh(languages, popularity)

# print(lang_counter.most_common(15))


plt.title("Most Popular Languages")
plt.ylabel("Programming languages")
plt.xlabel("No. of Users")

plt.tight_layout()

plt.show()
# print(x_indexes)