import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st

# Set the plot style to 'dark_background'
plt.style.use('dark_background')

# Load data from CSV file
df = pd.read_csv('master_plan_R1.csv')

# Clean up CAD column
df['CAD'] = df['CAD'].str.replace(',','').str.replace('$','').astype(float)

# Set x and y values
x_values = df['Month']
y_values = df['CAD']

# Plot the data as a line chart
fig, ax = plt.subplots()
ax.plot(x_values, y_values)

''' Another way to write this code would be: plt.plot(x_values, y_values)

But creating subplots we have more freedom to customize the plot

fig represents the entire plot area, and ax just the individual plots

fig = figure

ax = axes

'''

# Set chart title and axis labels
ax.set_title('Networth')
ax.set_xlabel('Date')
ax.set_ylabel('Value')

# Display the chart using Streamlit
st.pyplot(fig)
