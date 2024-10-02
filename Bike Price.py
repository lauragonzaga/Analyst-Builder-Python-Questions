import pandas as pd;

bikes_sold = inventory[(inventory['bike_sold'] == 'Y') & (inventory['bike_price'].notnull())]

avg_bike_price = bikes_sold['bike_price'].mean().round(2)
