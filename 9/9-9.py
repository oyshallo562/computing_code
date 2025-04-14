# 메뉴를 즐겨하는 함수 정의
def add_menu(menu_dict):
    while True:
        # 1) 새로 추가할 메뉴 이름을 입력받음
        menu_name = input("추가할 메뉴 이름을 입력하세요 (종료: exit) : ").strip()
        if menu_name.lower() == "exit":
            break

        # 2) 메뉴 이름이 이미 있었다면? -> 다시 입력받음
        if menu_name in menu_dict:
            print("이미 존재하는 메뉴이므로 다시 입력해주세요.")
            continue
        else:
            # 3) 메뉴 가격을 입력받음
            price_input = input("메뉴 가격을 입력하세요 : ").strip()
            try:
                menu_price = int(price_input)
            except:
                print("가격은 숫자여야 합니다!")
                continue
            if menu_price < 0:
                print("가격은 0 이상이어야 합니다!")
                continue
            menu_dict[menu_name] = menu_price

def cafe_menu(cafe_menu_dict):
    add_menu(cafe_menu_dict)
    print("새 메뉴 딕트 :", cafe_menu_dict)

cafe_menu_dict = { }

add_menu(cafe_menu_dict)
print("최종 메뉴 딕트 :", cafe_menu_dict)