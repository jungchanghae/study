# 180
"""
Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    result = []
    # 만약 비어있으면 바로 반환
    if len(logs) == 0:
        return pd.DataFrame(result, columns=['ConsecutiveNums']).astype({'ConsecutiveNums':'Int64'})
    
    prev_num = logs['num'].iloc[0]
    cnt = 0
    for idx in range(len(logs)):
        if prev_num == logs['num'].iloc[idx]:
            cnt += 1
            if cnt == 3:
                result.append(logs['num'].iloc[idx])
        else:
            cnt = 1
            prev_num = logs['num'].iloc[idx]
        
    return pd.DataFrame(result, columns=['ConsecutiveNums']).astype({'ConsecutiveNums':'Int64'}).drop_duplicates(keep='first')

if __name__=="__main__":
    data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
    # data = [[1, 0], [2, 0], [3, 0], [4, 0]]
    logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})
    print(consecutive_numbers(logs))