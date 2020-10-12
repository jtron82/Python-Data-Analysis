from data import *
import matplotlib.pyplot as plt 
 
dataframe = df[['primary_type']]
all_crime_count = pd.DataFrame(dataframe.groupby('primary_type').size().sort_values(ascending=True).rename('Crime Count'))
data = all_crime_count.iloc[-15:-1]

print(data[::-1])

data.plot(kind='barh')

plt.title("Horizontal Bar Chart")
plt.xlabel("All Crimes")
plt.ylabel("Crime Count Within My Location")
plt.subplots_adjust(left=0.48, right=0.98, top=0.93, bottom=0.11)

plt.show()