# 한-영 단어 사전을 정의
dictionary = {
    "사과": "apple",
    "바나나": "banana",
    "오렌지": "orange",
    "딸기": "strawberry",
    "포도": "grape"
}

# 단어를 번역하는 함수 정의
def translate_word(dic):
    while True:
        # 번역 가능한 단어 목록 출력
        words = list(dictionary.keys())
        print(f"번역할 단어 => {words}")

        # 사용자로부터 번역할 단어 입력 받기
        korean_word = input("번역할 한글 단어를 입력하세요 (종료하려면 q 입력): ")

        # 사용자가 'q'를 입력하면 종료
        if korean_word == "q":
            break

        # 입력된 단어가 사전에 있으면 번역 출력
        if korean_word in dic:
            print(f"{korean_word} : {dic[korean_word]}")
        else:
            # 사전에 없는 단어일 경우 안내 메시지 출력
            print("단어를 찾을 수 없습니다.")

# 함수 실행
translate_word(dictionary)
