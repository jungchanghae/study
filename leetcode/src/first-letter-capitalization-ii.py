"""
Write a solution to transform the text in the content_text column by applying the following rules:

- Convert the first letter of each word to uppercase and the remaining letters to lowercase
- Special handling for words containing special characters:
    - For words connected with a hyphen -, both parts should be capitalized (e.g., top-rated → Top-Rated)
- All other formatting and spacing should remain unchanged
Return the result table that includes both the original content_text and the modified text following the above rules.

The result format is in the following example.
"""


import pandas as pd

"""
string을 모두 lower로 변경한 후 시작 단어와 - 다음 단어를 대문자로 변경
"""

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    results = []
    
    for idx in range(len(user_content)):
        content_id = user_content.iloc[idx]['content_id']
        original_text = user_content.iloc[idx]['content_text']
        converted_text = format_string(original_text)
        results.append([content_id,original_text,converted_text])
        
    return pd.DataFrame(results, columns=['content_id', 'original_text', 'converted_text']).astype({'content_id':'Int64', 'original_text':'object', 'converted_text':'object'})
    

def format_string(s):
    # 문자열을 소문자로 변환
    s = s.lower()
    
    # 공백으로 분리한 후 각 단어 처리
    words = s.split()
    formatted_words = []
    
    for word in words:
        # 하이픈으로 분리된 단어는 각각 처리
        parts = word.split('-')
        capitalized_parts = [part.capitalize() for part in parts]
        formatted_words.append('-'.join(capitalized_parts))
    
    # 공백으로 다시 합치기
    return ' '.join(formatted_words)

if __name__ == '__main__':
    data = [[1, 'hello world of SQL'], [2, 'the QUICK-brown fox'], [3, 'modern-day DATA science'], [4, 'web-based FRONT-end development']]
    user_content = pd.DataFrame(data,columns=['content_id', 'content_text']).astype({'content_id':'Int64', 'content_text':'object'})
    print(capitalize_content(user_content))