import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x1 = [1,2,3,4,5,6]
y1 = [2,4,6,-8,-10,-12]
x2 = [3,6,9,12,15,18]
y2 = [1,3,5,8,9,10]

# To show the plot a line chart for the graph
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.title("Matplotlib Chart")
plt.legend(['Line 1', 'Line 2'])
sns.set_style('darkgrid')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.figure(figsize=(15,15))
plt.show()

