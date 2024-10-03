import pandas as pd;

tech_layoffs['percentage_laid_off'] = round(tech_layoffs['employees_fired'] / tech_layoffs['company_size']  * 100,2)

tech_layoffs[['company', 'percentage_laid_off']].sort_values(by = 'company')
