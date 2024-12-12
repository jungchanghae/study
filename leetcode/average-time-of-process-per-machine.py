# 1661
"""
There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.

The result format is in the following example.


"""

import pandas as pd

"""
Machine ID를 기준으로 Split을 먼저 해야한다. -> Machine ID unique를 먼저 List로 저장
각 Machine ID별로 Process_id를 가져오고, List로 사용해서 For문 돌리기 -> 각각의 시간차를 더한다.
Process_id 개수로 시간차를 나눠주고 result에 넣어준다.
"""
def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    results = []
    machine_ids = activity['machine_id'].unique() # MachineID를 모두 받아온다.
    
    for machine_id in machine_ids:
        process_ids = activity[activity['machine_id'] == machine_id]['process_id'].unique() # 각 MachineID별 ProcessID를 저장
        processing_time = 0
        for process_id in process_ids:
            processing_time += activity[(activity['machine_id'] == machine_id)&(activity['process_id'] == process_id)&(activity['activity_type'] == 'end')]['timestamp'].iloc[0] - activity[(activity['machine_id'] == machine_id)&(activity['process_id'] == process_id)&(activity['activity_type'] == 'start')]['timestamp'].iloc[0]
            
        results.append([machine_id, round(processing_time / len(process_ids),3)])
    return pd.DataFrame(results, columns=['machine_id', 'processing_time']).astype({'machine_id':'Int64', 'processing_time':'Float64'})

if __name__=="__main__":
    data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]
    activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})
    print(get_average_time(activity))