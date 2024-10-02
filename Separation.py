import pandas as pd;

bad_data.head()

bad_data['only_id'] = bad_data['id'].str[:5]

bad_data['name'] = bad_data['id'].str[5:]

bad_data[['only_id', 'name']]
