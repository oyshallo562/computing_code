# it조건문, random모듈, time모듈을 이용한 간단한 타자 게임 만들기
import random
import time

#게임을 위한 단어 리스트를 정의
words= ['컴퓨터', '타자', '대학교', '파이썬', 'Python', '알고리즘', '노트북', 'AI']
n=1

# 플레이어의 이름을 요청합니다
name = input("이름을 입력하세요=>")

print("타자 게임 준비되면 Enter~")
input()

# 사용자가 엔터 키를 누를 때까지 대기
start_time = time.time()

#게임 시작 시간을 기록

while n <= 3:     # 고정된 라운드 수를 위해 반복문을 사용(원하는 수 만큼 설정)
    print(f"* 라운드 {n}*")
    current_word = random.choice(words)
    # 리스트에서 무작위로 단어를 선택
    print(f"단어: {current_word}")
    # 플레이어에게 단어를 보여줍니다.
    user_input = input("단어를 입력하세요: ") # 사용자의 입력을 받습니다.
    if user_input == current_word:
        print("정답~")
        n = n + 1
    else:
        print("오타입니다. 다시 도전하세요~")

end_time = time.time() # 게임 종료 시간을 기록
es_time = end_time - start_time # 총 소요 시간을 계산
print(f"{name}'s 타이핑 시간 : {es_time:.21f} 초")
print("%s님의 타자 시간은 %.2f초" % (name, es_time))