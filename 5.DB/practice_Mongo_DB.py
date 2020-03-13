# import pymongo
# 변수 = pymongo.MongoClient("ip주소", "포트번호")

from pymongo import MongoClient
# 데이터베이스 연결 및 생성
con = MongoClient()
#print(con)

db = con.mymongo
# 컬렉션 연결및 생성
collection = db.sample

dict1 = {"name":"lee", "score": 90}
dict2 = {"name":"ru", "score": 92}
dict3 = {"name":"KIN", "score": 95}

li = [dict1, dict2]

collection.insert_one(dict3)
collection.insert_many(li)

# 데이터 조회
# 자료형을 확인해라. ( 강사님 당부 )
# find_one 은 dict다. 바로 출력해도 되겠다. dict['key' ] 를 이용 해서 부분적 사용가능
result = collection.find_one()
print(type(result))
print(result)

result = collection.find()
print(type(result))
# 자료형이 모르는 클래스라서 사용 가능한 속성을 확인
# iterator , __iter__ <-여러개의 데이터가 순서대로
# __iter__ 가 있으면 for - in 사용 가능
print(dir(result))
for temp in result :
    print(temp)

# name 이 KIN 인 데이터의 score 를 50 으로 변경
collection.update_one({"name":"KIN"}, {"$set":{"score":50}})
result = collection.find({"name":"KIN"})
for temp in result :
    print(temp)

# 삭제
collection.delete_one({"name":"KIN"})
result = collection.find()
for temp in result :
    print(temp)





