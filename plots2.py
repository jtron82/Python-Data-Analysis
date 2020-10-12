from data import *
import matplotlib.pyplot as plt 
 
dataframe = df[['primary_type']]
bottom_crime_count = pd.DataFrame(dataframe.groupby('primary_type').size().sort_values(ascending=True).rename('Crime Count'))
data = bottom_crime_count.iloc[-13:-8]

print(data[::-1])

data.plot(kind='bar')

plt.title("Bar Chart")
plt.ylabel("Bottom 5 Various Crimes")
plt.xlabel("Crime Count Within My Location")
plt.subplots_adjust(left=0.10, right=0.96, top=0.95, bottom=0.62) 

plt.show()