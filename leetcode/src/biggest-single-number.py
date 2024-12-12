# 619
"""
A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.

The result format is in the following example.
"""

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    if len(list(my_numbers.value_counts()[my_numbers.value_counts()==1].keys())) == 0:
        result = [None]
    else: 
        result = [max(list(my_numbers.value_counts()[my_numbers.value_counts()==1].keys()))[0]]
    return pd.DataFrame(result, columns=['num']).astype({'num':'Int64'})

if __name__=="__main__":
    data = [[8], [8], [3], [3], [1], [4], [5], [6]]
    my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})
    print(biggest_single_number(my_numbers))