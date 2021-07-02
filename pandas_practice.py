from datetime import time
from os import name
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)


aaa = pd.Series(['하나','둘','셋'], index = [1,2,3])
# print(aaa.values)
# print(aaa.index)
# print(aaa.value_counts)

s = pd.Series([1,np.nan,3,4,5,np.nan])
# print(s.count())
# s.fillna('하하하',inplace=True)
s.dropna(inplace=True)
# print(s)


# 특정 날짜를 기준으로 dataframe 생성

datas = pd.date_range('20120628',periods=5)
# print(datas)

# 난수 발생
r_list = np.random.randn(5,5)
# print(r_list)

rdf = pd.DataFrame(r_list,index=datas) # index를 datas로, 나머지 data들은 난수로
# print(rdf)

rdf = pd.DataFrame(r_list,index=datas, columns=['a','b','c','d','e'])
# print(rdf)
# print(rdf.values, rdf.index,rdf.columns)

rdf.sort_values(by='a')
# print(rdf[['b','c']])
# print(rdf[0:3])

# print(rdf.iloc[0:2,0:2])
# print(rdf.info())

ppp = ([['이순신', '2021-01-01 9:10', 'happy@gmail.com '],
       ['홍길동', '2021-01-08 9:20', '  1004@NAVER.COM'],
       ['유관순', '2021-02-01 10:20', ' Iron at yahoo.co.kr '],
       ['이이', '2021-02-02 11:40', 'lee@gmail.com'],
       ['김구', '2021-02-28 15:10', 'kim@daum.net'],
       ['윤봉길', '2021-04-10 19:20', 'yeon@daum.ac.kr'],
       ['강감찬', '2021-06-30 21:20', 'kkc@gmail.com'],
       ['신사임당', '2021-07-20 23:30', 'monther@NAVER.COM '],
       ['을지문덕', '2021-08-28 11:48', '    ygmd@daum.net'],
       ['유재석', '2021-09-01 3:12', 'yjs at gmail.com']])

ppp = pd.DataFrame(ppp,columns=['name','birth','email'])
# print(ppp.loc[1,['email']])
# print("-"*30)
# print(ppp.iloc[1,2])
# print("-"*30)
# print(ppp['name'])

friend_dict_list = [{'name': '신동엽', 'age': 20, 'job': '연예인', 'hobby':'music'},
                     {'name': '유재석', 'age': 41, 'job': '교수', 'hobby':'art'},
                     {'name': '김새롬', 'age': 18, 'job': '학생', 'hobby':'study'},
                     {'name': '이영자', 'age' : 45, 'job': '상담사', 'hobby' : 'talk'},
                     {'name' :  '강호동', 'age' : 38, 'job' : '연예인', 'hobby' : 'talk'}]

friend = pd.DataFrame(friend_dict_list)
friend = friend.append({'name' :  '이현수', 'age' : 31, 'job' : '학생', 'hobby' : 'coding'}, ignore_index=True)
friend = friend.append({'name' :  '이현수', 'age' : 31, 'job' : '학생', 'hobby' : 'coding'}, ignore_index=True)
friend['sal'] = 0

friend['sal'] = np.where(friend['job'] == '학생',100,200)
print(friend)

# print(friend.drop_duplicates(keep='last'))
# print(friend.isnull())
print(friend.groupby('age').mean())
print(friend['job'].unique())
