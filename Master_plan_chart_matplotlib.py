import pandas as pd
import matplotlib.pyplot as plt   

# Load data from CSV file into a pandas datafram

df = pd.read_csv('master_plan_R1.csv')

# Remove the commas and $ sign

df['CAD'] = df['CAD'].str.replace(',', '').str.replace('$','').astype(float)

# Get x and y values from the dataframe

x_values = df['Month']
y_values = df['CAD']

# Plot the data as a line chart

plt.plot(x_values, y_values)

# Set the chart title and axis labels

plt.title('Net Worth')
plt.xlabel('Date')
plt.ylabel('Value')

# Display the chart

plt.show()
