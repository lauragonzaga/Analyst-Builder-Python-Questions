import pandas as pd;


managers = direct_reports[direct_reports['position'].str.contains('Manager')]

direct_reports_count = direct_reports['managers_id'].value_counts().reset_index()

manager_reports = managers.merge(direct_reports_count, left_on='employee_id', right_on='managers_id', how='left')

manager_reports[['employee_id', 'position', 'count']].rename(columns = {'employee_id': 'manager_id'})
