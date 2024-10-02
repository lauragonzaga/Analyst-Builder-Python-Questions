import pandas as pd;

customers.head()

customers['first_name'] = customers['full_name'].str.split(' ', expand = True)[0]

customers[['customer_id', 'first_name']]
