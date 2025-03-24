import time
import random

word_list_lv1 = ["사과", "바나나", "고양이", "파이썬", "게임", "프로그래밍", "컴퓨터", "노트북", "모니터", "키보드", "마우스", "피자", "햄버거", "치킨", "커피"]
word_list_lv2 = ["사과나무", "바나나나무", "고양이사료", "파이썬프로그래밍", "게임컴퓨터", "프로그래밍노트북", "컴퓨터모니터", "노트북키보드", "모니터마우스", "키보드피자", "마우스햄버거", "피자치킨", "햄버거커피", "치킨사이다", "커피우유"]
word_list_lv3 = ["Python", "Java", "C", "C++", "C#", "JavaScript", "HTML", "CSS", "PHP", "Ruby", "Swift", "Kotlin", "R", "Go", "Scala", "Perl"]
word_list_lv4 = ["PythonProgramming", "JavaProgramming", "CProgramming", "C++Programming", "C#Programming", "JavaScriptProgramming", "HTMLProgramming", "CSSProgramming", "PHPProgramming"]

score = 0
n = 1

name = input("이름을 입력하세요=> ")
print("타자 게임 준비되면 Enter~")
input()

start_time = time.time()

while n <= 10 :
    print(f"* 라운드 {n}*")
    current_word = random.choice(word_list_lv1)
    # 리스트에서 무작위로 단어를 선택
    print(f"단어: {current_word}")
    # 플레이어에게 단어를 보여줍니다.
    user_input = input("단어를 입력하세요: ") # 사용자의 입력을 받습니다.
    if user_input == current_word:
        print("정답~")
        score = score + 10
    else:
        print("오타입니다. 다시 도전하세요~")
        score = score - 5
    n = n + 1

if score > 90:
    print("다음 라운드 도전?")
    next = input("다음 라운드 도전? (Y/N)")
    if next == "Y":
        n = 1
        while n <= 10:
            print(f"* 라운드 {n}*")
            current_word = random.choice(word_list_lv2)
            # 리스트에서 무작위로 단어를 선택
            print(f"단어: {current_word}")
            # 플레이어에게 단어를 보여줍니다.
            user_input = input("단어를 입력하세요: ") # 사용자의 입력을 받습니다.
            if user_input == current_word:
                print("정답~")
                score = score + 10
            else:
                print("오타입니다. 다시 도전하세요~")
                score = score - 5
            n = n + 1
    else:
        print("수고하셨습니다.")

if score > 180:
    next = input("다음 레벨 도전? (Y/N)")
    if next == "Y":
        n = 1
        while n <= 10:
            print(f"* 라운드 {n}*")
            current_word = random.choice(word_list_lv3)
            # 리스트에서 무작위로 단어를 선택
            print(f"단어: {current_word}")
            # 플레이어에게 단어를 보여줍니다.
            user_input = input("단어를 입력하세요: ") # 사용자의 입력을 받습니다.
            if user_input == current_word:
                print("정답~")
                score = score + 10
            else:
                print("오타입니다. 다시 도전하세요~")
                score = score - 5
            n = n + 1
    else:
        print("수고하셨습니다.")

if score > 270:
    print("다음 라운드 도전?")
    next = input("다음 레벨 도전? (Y/N)")
    if next == "Y":
        n = 1
        while n <= 10:
            print(f"* 라운드 {n}*")
            current_word = random.choice(word_list_lv4)
            # 리스트에서 무작위로 단어를 선택
            print(f"단어: {current_word}")
            # 플레이어에게 단어를 보여줍니다.
            user_input = input("단어를 입력하세요: ") # 사용자의 입력을 받습니다.
            if user_input == current_word:
                print("정답~")
                score = score + 10
            else:
                print("오타입니다. 다시 도전하세요~")
                score = score - 5
            n = n + 1
    else:
        print("수고하셨습니다.")

# 게임 종료 시간
end_time = time.time()

# 걸린 시간 계산
elapsed_time = end_time - start_time

# 결과 출력
end_time = time.time() # 게임 종료 시간을 기록
es_time = end_time - start_time # 총 소요 시간을 계산
print(f"{name}'s 타이핑 시간 : {es_time:.2f} 초/ 점수는 {score}")
print("%s님의 타자 시간은 %.2f초/ 점수는 %d" % (name, es_time, score))