import matplotlib.pyplot as plt
import numpy as np
import sys
import datetime

x = np.arange(1, 10)
y = np.square(x)
plt.plot(x, y)
plt.savefig(sys.argv[1])
