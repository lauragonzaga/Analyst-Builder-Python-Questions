import pandas as pd;

employees.head()

def new_salary(row):
  if row['pay_level'] == 1:
    return row['salary'] * 1.1
  elif row['pay_level'] == 2:
    return row['salary'] * 1.15
  elif row['pay_level'] == 3:
    return row['salary'] * 3

employees['new_salary'] = employees.apply(new_salary, axis = 1)

employees
