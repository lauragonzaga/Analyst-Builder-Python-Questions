import pandas as pd;

has_member_card = customers[customers['has_member_card'] == 'Y'].count()['kroger_id'] 

total_count = customers['kroger_id'].count()


percentage = round(has_member_card / total_count * 100, 2)
