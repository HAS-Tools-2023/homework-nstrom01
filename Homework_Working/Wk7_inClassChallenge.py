
#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Import the flow data to use
data = pd.read_table("./streamflow_demo.txt", sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#%% Graph 3 -- OG
mybins = np.linspace(0, np.log10(np.max(data["flow"])), num=15)
plt.hist(np.log10(data["flow"]), bins=mybins)
plt.title('Streamflow')
plt.ylabel('Count')

#%%
mybins = np.linspace(0, np.log10(np.max(data["flow"])), num=1000)
plt.hist(np.log10(data["flow"]), bins=mybins, color='pink')
plt.title('Streamflow')
plt.ylabel('Count')


# %%
mybins = np.linspace(0, np.log10(np.min(data["flow"])), num=15)
plt.hist(np.log10(data["flow"]), bins=mybins)
plt.title('Streamflow')
plt.ylabel('Count')


# %% Plot 2 edited 

## Import the flow data to use
data = pd.read_table("./streamflow_demo.txt"
                     ,sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
                     )
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

ax=data.plot.scatter(x='year', y='flow',
c='year', colormap='prism', marker='x')
ax.set_title("Monthly stream Flow")

# %% Plot 1 edited
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
y1=np.sin(x)
y2=np.cos(x)
y3= (x**3)
ax = plt.axes()
ax.plot(x, y1, linestyle='dashed', label='sinx')
ax.plot(x, y2, label='cosx')
ax.plot(x, y3, label = 'x^3')
ax.legend(loc='upper right')
plt.title('Sine vs Cosine Waves')
plt.xlabel('x axis')



# %%
