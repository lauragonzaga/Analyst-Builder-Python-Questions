import pandas as pd;


products['Shrinkflation_Flag'] = (products['original_size'] > products['new_size']) & (products['original_price'] <= products['new_price'])

products['Shrinkflation_Flag'] = products['Shrinkflation_Flag'].map({True: 'True'})


products['size_change_percentage'] = (products['new_size'] - products['original_size']) / products['original_size'] * 100

products['price_change_percentage'] = (products['new_price'] - products['original_price']) / products['original_price'] * 100

products[['product_name', 'size_change_percentage', 'price_change_percentage', 'Shrinkflation_Flag']].sort_values(by= 'product_name')
