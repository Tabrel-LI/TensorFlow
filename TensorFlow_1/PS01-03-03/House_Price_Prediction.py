#
# This is a very simple prediction of house prices based on house size,
#  implemented in TensorFlow.
#

import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import random as np_random

# Generate some house sizes between 1000 and 3500 sq ft.
num_house = 160
np.random.seed(42)
#house_size = np.random.randint(low=1000, high=3500, size=num_house)
house_size = np_random.randint(low=1000, high=3500, size=num_house)

# Generate house prices from house size with a random noise added.
np.random.seed(42)
#house_price = house_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_house)
house_price = house_size * 100.0 + np_random.randint(low=20000, high=70000, size=num_house)

# Plot generated house and size data.
plt.plot(house_size, house_price, "bx")  # bx = blue x
plt.ylabel("Price")
plt.xlabel("Size")
plt.show()
