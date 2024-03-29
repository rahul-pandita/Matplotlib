from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60, 40]
labels = ["Sixty","Forty"]

plt.pie(slices, labels=labels)

plt.title("Pie Chart")
plt.tight_layout()
plt.show()