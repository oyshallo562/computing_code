# 딕셔너리 만들기
person = {"name": "홍길동", "age": 20, "city": "Seoul"}
print ("자료=>", person)

# 딕셔너리에서 쌍 추가하기
person['pn'] = "010-1234-5678"
print("추가=>", person)

# 딕셔너리에서 쌍 삭제하기
del person['pn']
print("삭제=>", person)
