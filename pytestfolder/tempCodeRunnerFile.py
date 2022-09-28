import numpy as np
import matplotlib.pyplot as plt

x = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
y=[1, 2, 3, 4, 5, 6, 7, 8]

plt.figure()
plt.bar(x, y, alpha=0.2)
plt.title(f"data")
plt.xlabel("X")
plt.ylabel("Y")
plt.xticks(x, [str(i) for i in x], rotation=30)
plt.tick_params(axis='x', which='both', labelsize=11)
plt.tight_layout()
plt.show()