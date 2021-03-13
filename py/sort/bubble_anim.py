import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yaml

with open("sort_anim.yaml") as config_file:
    config = yaml.load(config_file, Loader = yaml.FullLoader)

LOW = config["LOW"]
HIGH = config["HIGH"]
SIZE = config["SIZE"]
SAVE = config["SAVE"]

def bubble_sort_step(array):
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
    return array

fig = plt.figure()

array1 = np.random.randint(low = LOW, high = HIGH, size = SIZE)
x = np.linspace(0, len(array1), len(array1))
bars = plt.bar(x,array1)

def animate(i):
    global array1
    array1 = bubble_sort_step(array1)
    for j, b in enumerate(bars):
        b.set_height(array1[j]) 

anim = FuncAnimation(fig, animate)

if SAVE:
    anim.save('bubble_sort.mp4', fps = 16)
else:
    plt.show()