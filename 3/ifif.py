user_list = ["이서원", "오유성", "김승연", "전지윤"]
user_id = input("이름을 입력하세요 : ").strip()

if user_id in user_list:
    pw = input("비밀번호를 입력하세요 : ")

    if pw == "1234":
        print("환영합니다.")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("존재하지 않는 사용자입니다.")