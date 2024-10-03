import pandas as pd;

linkedin_posts['popularity'] = linkedin_posts['actions'] / linkedin_posts['impressions'] * 100


high_popularity= linkedin_posts[linkedin_posts['popularity'] >= 1].sort_values(by = 'popularity', ascending = False)



pd.DataFrame(high_popularity[['post_id', 'popularity']])
