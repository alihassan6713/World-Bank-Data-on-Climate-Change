# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to clean the World Bank data
def clean_world_bank_data(filename):
    # Read the CSV file and set 'Country Name' and 'Indicator Name' as index
    df = pd.read_csv(filename, index_col=['Country Name', 'Indicator Name'])
    # Drop the unnecessary columns 'Country Code' and 'Indicator Code'
    df = df.drop(columns=['Country Code', 'Indicator Code'])
    # Convert the data to numeric type, and replace any missing values using forward and backward fill
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(method='ffill', axis=0).fillna(method='bfill', axis=0)
    # Reset the index of the DataFrame
    df = df.reset_index()
    return df

# Define the filename to read
filename = 'mainfile.csv'

# Call the function to clean the data and store it in a variable
world_bank_data = clean_world_bank_data(filename)

# Transpose the data
world_bank_data_t = world_bank_data.transpose()
print(world_bank_data_t)

# Define the indicators of interest
total_population = 'Population, total'
co2_emissions = 'CO2 emissions (kt)'
greenhouse_gasses = 'Total greenhouse gas emissions (kt of CO2 equivalent)'

# Get the statistics for the selected indicators
total_population_stats = world_bank_data[world_bank_data['Indicator Name'] == total_population]
emmision_stats = world_bank_data[world_bank_data['Indicator Name'] == co2_emissions]
greenhouse_gasses_stats = world_bank_data[world_bank_data['Indicator Name'] == greenhouse_gasses]

# Print the statistics for the selected indicators
print('Total population emissions statistics:')
print(total_population_stats.describe())
print('\nCO2 emissions statistics:')
print(emmision_stats.describe())
print('\nGreenhouse gas emissions statistics:')
print(greenhouse_gasses_stats.describe())

# Plot CO2 emissions over time for selected countries
countries = ['Arab World', 'United Kingdom', 'United Arab Emirates', 'Iraq']
for country in countries:
    # Get the CO2 emissions statistics for the country
    co2_stats_temp = world_bank_data[world_bank_data['Country Name'] == country]
    co_stats_temp = co2_stats_temp.describe()
    # Plot the CO2 emissions for the country
    co2_stats_temp.plot(label=country, legend=False)
    plt.title('CO2 emissions over time for countries')
    plt.xlabel('Year')
    plt.ylabel('CO2 emissions (in KT)')
    plt.show()

# Concatenate the statistics for the selected indicators
combined_df = pd.concat([total_population_stats.describe(), emmision_stats.describe(), greenhouse_gasses_stats.describe()])
# Calculate the correlation matrix for the selected indicators
correlation_matrix = combined_df.corr()

# Print the correlation matrix
print('Correlation matrix:')
print(correlation_matrix)

# Plot scatter plots to visualize the relationship between CO2 emissions and the selected indicators
plt.scatter(emmision_stats.describe(), total_population_stats.describe())
plt.title('CO2 emissions vs total population')
plt.xlabel('CO2 emissions (in KT)')
plt.ylabel('Total population')
plt.show()

plt.scatter(emmision_stats.describe(), greenhouse_gasses_stats.describe())
plt.title('CO2 emissions vs greenhouse gas emissions')
plt.xlabel('CO2 emissions (in KT)')
plt.ylabel('Greenhouse gas emissions (in KT)')
plt.show()

# Plot a bar graph to visualize the CO2 emissions statistics
co2_stats_desc = greenhouse_gasses_stats.describe()
co2_stats_desc = co2_stats_desc.loc[['mean', 'std']]
co2_stats_desc.plot(kind='bar', legend=False)
plt.title('CO2 emissions statistics')
plt.ylabel('CO2 emissions (in KT)')
plt.show()

# visualize the correlation matrix for each indicator for each country using a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
