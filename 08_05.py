import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

animals = ['cat', 'dog', 'olaagh', 'khaar']
heights = [30, 80, 150, 60]
weights = [5, 40, 400, 50]

fig, ax = plt.subplots()
x = np.arange(len(heights))
width = 0.40

ax.bar(x-0.2, heights, width, color='red')
ax.bar(x+0.2, weights, width, color='orange')

ax.legend(['height', 'weight'])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)

explode = [0.2, 0.1, 0.1, 0.1]
plot_pi, ax = plt.subplots()
ax.pie(heights, explode=explode, labels=animals, autopct='%1.1f%%', shadow=True)
# ax.pie(heights, labels=animals, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(plot_pi)