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

print(lang_counter)


# plt.title("Median Salary (USD) by Age")
# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")

# plt.tight_layout()

# plt.show()
# print(x_indexes)