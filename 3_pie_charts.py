from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices, labels=labels, explode=explode, shadow=True, autopct="%1.1f%%",wedgeprops={"edgecolor": "black"})

plt.title("Pie Chart")
plt.tight_layout()
plt.show()