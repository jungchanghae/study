# 262
"""
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

Return the result table in any order.

The result format is in the following example.
"""

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    results = [] # 결과 저장
    
    # Data Filtering 작업
    banned_user_ids = users.loc[users['banned'].str.contains(r'Yes')]['users_id'].unique() # 밴 당한 id는 제거하기 위한 list
    trips = trips.loc[(~trips['client_id'].isin(banned_user_ids)) & (~trips['driver_id'].isin(banned_user_ids))] # ban list에 있는 것들은 지우고 계산
    trips = trips.loc[(trips['request_at']>='2013-10-01') & (trips['request_at']<='2013-10-03')] # 정해진 날짜만 살펴봐야함
    
    date_list = trips['request_at'].unique() # 날짜별로 검색해야하므로 list로 선언
    for date in date_list:
        date_df = trips.loc[trips['request_at'] == date] # 특정 날짜에서 검색과 계산이 이루어져야하므로 sub dataframe을 만듬
        total_cnt = len(date_df) # 전체 개수
        cancel_cnt = len(date_df.loc[date_df['status'].str.contains(r'cancelled_by_*')]) # 취소된 건 확인
        if total_cnt == 0: # 건수가 없는 경우 패스
            pass
        else:
            results.append([date,round(cancel_cnt/total_cnt,2)])

    return  pd.DataFrame(results, columns=['Day', 'Cancellation Rate']).astype({'Day':'object', 'Cancellation Rate':'Float64'})



if __name__=='__main__':
    data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
    trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object', 'request_at':'object'})

    data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
    users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})
    print(trips_and_users(trips, users))