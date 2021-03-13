import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
array1 = np.array([3,6,8,3,4,6,2])
frames = 100
x = np.linspace(0, len(array1), len(array1))
barcollection = plt.bar(x,array1)

for i, b in enumerate(barcollection):
    print(i, b)