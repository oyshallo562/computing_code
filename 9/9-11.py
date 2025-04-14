dictionary = {}

# 단어 추가 함수
def add_word(dic):
    korean_word = input("한글 단어를 입력하세요: ")
    english_word = input("영어 단어를 입력하세요: ")
    dic[korean_word] = english_word

# 단어 검색 함수
def search_word(dic):
    korean_word = input("검색할 한글 단어를 입력하세요: ")
    if korean_word in dic:
        print(f"{korean_word}: {dic[korean_word]}")
    else:
        print(f"{korean_word} 단어가 사전에 없습니다.")

# 단어 수정 함수
def modify_word(dic):
    korean_word = input("수정할 한글 단어를 입력하세요: ")
    if korean_word in dic:
        english_word = input("새로운 영어 단어를 입력하세요: ")
        dic[korean_word] = english_word
        print(f"{korean_word} 단어가 수정되었습니다.")
    else:
        print(f"{korean_word} 단어가 사전에 없습니다.")

# 단어 삭제 함수
def delete_word(dic):
    korean_word = input("삭제할 한글 단어를 입력하세요: ")
    if korean_word in dic:
        del dic[korean_word]
        print(f"{korean_word} 단어가 삭제되었습니다.")
    else:
        print(f"{korean_word} 단어가 사전에 없습니다.")

# 메뉴 선택
while True:
    print("1. 단어 추가")
    print("2. 단어 검색")
    print("3. 단어 수정")
    print("4. 단어 삭제")
    print("5. 종료")
    choice = input("원하는 작업을 선택하세요: ")

    if choice == "1":
        add_word(dictionary)
    elif choice == "2":
        search_word(dictionary)
    elif choice == "3":
        modify_word(dictionary)
    elif choice == "4":
        delete_word(dictionary)
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
