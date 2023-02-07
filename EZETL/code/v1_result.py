import pandas as pd
import matplotlib.pyplot as plt

# Extract
df = pd.read_csv('input_g.csv')

# Transform
df['sales'] = df['sales'].str.replace('$', '').str.replace(',', '').astype(float)

# Load
df.plot(x='year', y='sales', kind='bar')
plt.savefig('output.png')