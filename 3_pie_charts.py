from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60, 40, 120, 90]
labels = ["Sixty","Forty", "Extra1", "Extra2"]
colors = ["blue", "red", "green", "yellow"]

plt.pie(slices, labels=labels, colors=colors, wedgeprops={"edgecolor": "black"})

plt.title("Pie Chart")
plt.tight_layout()
plt.show()