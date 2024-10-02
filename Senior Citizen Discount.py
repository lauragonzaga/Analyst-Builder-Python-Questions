import pandas as pd;

customers['age'] = pd.to_datetime('1/1/2023') - pd.to_datetime(customers['birth_date'])

customers['age'] = customers['age'].dt.days // 365

seniors = customers[customers['age'] >= 55].sort_values(by= 'customer_id')['customer_id']

pd.DataFrame(seniors)
