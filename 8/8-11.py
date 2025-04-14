import random

def recommend_lunch():
    # 점심 메뉴 추천
    lunch_options = ["김밥", "라면", "비빔밥", "떡볶이", "피자", "햄버거"]
    print("추천 점심 메뉴:", random.choice(lunch_options))

recommend_lunch()