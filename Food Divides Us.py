import pandas as pd;

regions = food_regions.groupby('region')['fast_food_millions'].sum().reset_index().sort_values(by = 'fast_food_millions', ascending = False)['region'].head(1)

pd.DataFrame(regions)
