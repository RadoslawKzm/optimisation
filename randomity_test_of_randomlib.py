import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
# pip install --only-binary :all: mysqlclient
import random
import collections

rand_range = (0, 100)
sample_size = 100_000

gen = (random.randint(rand_range[0], rand_range[1]) for x in range(sample_size))
cnt = collections.Counter(gen)

plt.bar(cnt.keys(), cnt.values())
plt.title('testing')
plt.show()

'''
Random lib is albost truly random, doesnt produce gaussian probability distribution
'''