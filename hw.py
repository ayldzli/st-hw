import matplotlib.pyplot as plt
import numpy as np

flips = np.random.choice(
    ["Heads", "Tails"],
    size=10000,
    p=[0.5, 0.5]
)

x, y = np.unique(flips, return_counts=True)
bars = plt.bar(x, y, color=["red", "blue"])

plt.text(
    bars[0].get_x() + bars[0].get_width() / 2,
    bars[0].get_height() + 10,
    f"{x[0]}: {int(y[0])}",
    ha="center"
)

plt.text(
    bars[1].get_x() + bars[1].get_width() / 2,
    bars[1].get_height() + 10,
    f"{x[1]}: {int(y[1])}",
    ha="center"
)

plt.show()
