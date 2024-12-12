# 185

"""
A company's executives are interested in seeing who earns the most money in each of the company's departments. 
A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    result_df = []
    
    # 애초에 빈 경우 제외
    if len(employee) == 0:
        return pd.DataFrame(result_df, columns=['Department', 'Employee', 'Salary']).astype({'Department':'object', 'Employee':'object', 'Salary':'Int64'})
    
    # 각 department 마다 작업하기 위한 for loop
    for idx in range(len(department)):
        departmentID, dep_name = department.iloc[idx]
        dep_df = employee.loc[employee['departmentId']==departmentID] # departmentID마다 작업하기 위한 sub dataframe
        
        # 해당 직업에 사람이 없는 경우
        if len(dep_df) == 0:
            continue
        
        # top-k 급여 확인 3개가 안되는 경우 가장 작은 값으로 설정
        salary_list = list(dep_df['salary'].unique())
        salary_list.sort(reverse=True)
        if len(salary_list) >= 3:
            top_three_salary = salary_list[2]
        else:
            top_three_salary = salary_list[-1]
            
        # 급여가 top_three_salary 이상인 행들만 남기기
        dep_df = dep_df.loc[dep_df['salary'] >= top_three_salary]
        dep_df['Department'] = dep_name
        dep_df.rename(columns={'name':'Employee','salary':'Salary'},inplace=True)
        
        result_df.append(dep_df.sort_values('Salary',ascending=False)[['Department','Employee','Salary']])
    
    if len(result_df) > 0:
        return pd.concat(result_df,ignore_index=True)
    else:
        return pd.DataFrame(result_df, columns=['Department', 'Employee', 'Salary']).astype({'Department':'object', 'Employee':'object', 'Salary':'Int64'})

if __name__ == '__main__':
    data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
    data = [[1, 'IT'], [2, 'Sales']]
    department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
    
    print(top_three_salaries(employee,department))