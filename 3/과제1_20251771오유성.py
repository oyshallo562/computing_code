import time

word_list = ["사과", "바나나", "고양이", "파이썬", "게임"]
score = 0

name = input("이름을 입력하세요=> ")
print("타자 게임 준비되면 Enter~")
input()

start_time = time.time()

for i, word in enumerate(word_list, start=1):
    print(f"* 라운드 {i} *")
    print(f"단어: {word}")
    user_input = input("단어를 입력하세요: ")

    if user_input == word:
        print("정답입니다.")
        score += 10
    else:
        print("오타입니다. 다시 도전하세요.")

# 게임 종료 시간
end_time = time.time()

# 걸린 시간 계산
elapsed_time = end_time - start_time

# 결과 출력
end_time = time.time() # 게임 종료 시간을 기록
es_time = end_time - start_time # 총 소요 시간을 계산
print(f"{name}'s 타이핑 시간 : {es_time:.2f} 초/ 점수는 {score}")
print("%s님의 타자 시간은 %.2f초/ 점수는 %d" % (name, es_time, score))
