# 1527
"""
Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    results = []
    
    for idx in range(len(patients)):
        data = patients.iloc[idx]
        # DIAB1이 포함되어 있을때만  result에 추가
        if ('DIAB1' == data['conditions'][:5]) or (' DIAB1' in data['conditions']):
            patient_id = data['patient_id']
            patient_name = data['patient_name']
            conditions = data['conditions']
            results.append([patient_id,patient_name,conditions])
    return pd.DataFrame(results, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'(^| )DIAB1')] # 새로 알게된 방법..

if __name__=="__main__":
    data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
    patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})
    print(find_patients(patients))