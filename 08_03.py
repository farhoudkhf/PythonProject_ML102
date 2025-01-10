# pip install pandas
# pip install numpy
# pip install streamlit
# pip install matplotlib

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

col_names = ['column1', 'column2', 'column3']

data = pd.DataFrame(np.random.randint(30, size=(30, 3)), columns=col_names)

'line gragh:'
st.line_chart(data)

'bar chart:'
st.bar_chart(data)

animals = ['cats', 'dogs', 'olaaagh']
heights = [30, 80, 150]

'pie chart:'
fig, ax = plt.subplots()
ax.pie(heights, labels=animals)

st.pyplot(fig)
