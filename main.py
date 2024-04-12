# Annotate Bars in a single-group Bar chart with Pandas and Matplotlib 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': [0.79, 0.62, 0.65, 0.22, 0.47],
    'y': [0.97, 0.26, 0.88, 0.63,  0.63],
}, index=['A', 'B', 'C', 'D', 'E'])

ax = df.plot.bar(x='x', y='y')

ax.bar_label(ax.containers[0])

plt.show()
