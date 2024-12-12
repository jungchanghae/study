# 601

"""
Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.
"""

"""
3번 이상 연속으로 100명 이상 방문한 날짜를 나열하라
"""

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    results = [] # 전체 저장
    cnt = 0
    tmp_list = [] # 임시로 저장할 곳
    
    for idx in range(len(stadium)):
        if stadium.iloc[idx]['people'] >= 100:
            tmp_list.append(list(stadium.iloc[idx][['id', 'visit_date', 'people']]))
            cnt += 1
        else:
            # 3 이상인 경우만 전체 결과에 넣기
            if cnt >= 3:
                results.extend(tmp_list)
            # 초기화
            tmp_list = []
            cnt = 0
    # 만약 loop 끝까지 추가만 된 경우
    if cnt >= 3:
        results.extend(tmp_list)    
    return pd.DataFrame(results, columns=['id', 'visit_date', 'people']).astype({'id':'Int64', 'visit_date':'datetime64[ns]', 'people':'Int64'})
    
if __name__=="__main__":
    data = [[1, '2017-01-01', 10], [2, '2017-01-02', 109], [3, '2017-01-03', 150], [4, '2017-01-04', 99], [5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]]
    stadium = pd.DataFrame(data, columns=['id', 'visit_date', 'people']).astype({'id':'Int64', 'visit_date':'datetime64[ns]', 'people':'Int64'})
    print(human_traffic(stadium))