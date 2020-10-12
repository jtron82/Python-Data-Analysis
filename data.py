import requests
import pandas as pd
import json

# Chicago Open Data Portal Crime API
baseurl = "https://data.cityofchicago.org/resource/w98m-zvie.json"

# data on crimes between specified date and time
datebetw = "?$where=date between '2019-01-01T12:00:00' and '2019-07-29T14:00:00'"

# longitude and latitute for designated area
boxurl = 'within_box(location, 41.992408, -87.716760, 42.040585, -87.782562)'

# concatenate variables to obtain various specified data
ourl = baseurl + datebetw + ' AND ' + boxurl

text =  requests.get(ourl).json()  
 
# create pandas dataframe dictionary container object 
df = pd.DataFrame(
    text, columns=['date', 'block', 'primary_type', 'description'])