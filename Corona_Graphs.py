import pandas as pd
import matplotlib.pyplot as plt

# Read cv files
portugal = pd.read_csv ('Corona_PT.csv')
uk = pd.read_csv('Corona_Uk.csv')

# Put everything from uk and portugal in dataframe df
df = pd.DataFrame(uk)
df2 = pd.DataFrame(portugal)
df['New cases PT']= df2['New Cases PT']
df['Total Cases PT']=df2['Total Cases PT']
df['Deaths PT']=df2['Deaths PT']
df['Total Deaths PT']=df2['Total Deaths PT']
df['(Total Deaths PT / Pop Total)*100'] = df2['(Total Deaths PT / Pop Total)*100']

# Delete last row in data frame due to messy data
df.drop(index=86, inplace = True)

# Figure1 plot cases and total cases UK and Portugal (4 subplots)
fig, axes = plt.subplots(nrows=2, ncols=2)
df.plot(x='date', y='New cases PT', ax=axes[0,0], legend = False); axes[0,0].set_title('New cases Portugal');
df.plot(x='date', y='Total Cases PT', ax=axes[0,1], legend = False); axes[0,1].set_title('Total cases Portugal')
df.plot(x='date', y='New cases UK', color = 'r', ax=axes[1,0], legend = False); axes[1,0].set_title('New cases UK')
df.plot(x='date', y='Total Cases UK', color = 'r', ax=axes[1,1], legend = False); axes[1,1].set_title('Total cases UK');
plt.subplots_adjust(wspace=0.35, hspace=0.35)   # Adjust spacing to avoid overlap of subplots
fig.savefig('figure1.png')

# Figure2 plot deaths and total deaths UK and Portugal (4 subplots)
fig, axes = plt.subplots(nrows=2, ncols=2)
df.plot(x='date', y='Deaths PT', ax=axes[0,0], legend = False); axes[0,0].set_title('Deaths Portugal');
df.plot(x='date', y='Total Deaths PT', ax=axes[0,1], legend = False); axes[0,1].set_title('Total Deaths Portugal')
df.plot(x='date', y='Deaths UK', color = 'r', ax=axes[1,0], legend = False); axes[1,0].set_title('Deaths UK')
df.plot(x='date', y='Total Deaths UK', color = 'r', ax=axes[1,1], legend = False); axes[1,1].set_title('Total Deaths UK');
plt.subplots_adjust(wspace=0.35, hspace=0.35)   # Adjust spacing to avoid overlap of subplots
fig.savefig('figure2.png')

# Figure3 Deaths per pop UK and PT on same plot
fig, ax = plt.subplots(1, figsize=(8, 6))   # Initialise the figure and axes.
fig.suptitle('Covid-19 deaths as a percentage of the country\'s entire population', fontsize=15)    # Set the title for the figure
df.plot(x='date', y='(Total Deaths PT / Pop Total)*100', ax=ax, color='r', label='Portugal')
df.plot(x='date', y='(total deaths / Pop Total)*100', ax=ax, color='b', label='UK')
plt.legend(loc="lower right", title="Country", frameon=False)   # Add a legend bottom right
fig.savefig('figure3.png')  # Save the figure

# Display figures
plt.show()