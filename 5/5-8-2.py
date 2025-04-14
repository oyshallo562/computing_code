import random

n = 1
score = 0
mistakes = 0  # 틀린 횟수를 저장하는 변수

print("문제를 시작하려면 Enter키를 치세요")
input()

print("이름입력 -> ", end="")
name = input()

# 연산자 선택
print("어떤 연산 문제를 풀고 싶으신가요?")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")
operator_choice = input("번호를 선택하세요 (1~4): ")

if operator_choice not in ['1', '2', '3', '4']:
    print("잘못된 선택입니다. 기본 연산(덧셈)으로 진행합니다.")
    operator_choice = '1'

print("문제를 10개 풀고 Enter키를 치세요")
input()

while n <= 10:
    # 연산에 따라 문제 생성
    if operator_choice == '1':  # 덧셈
        x = random.randint(1, 99)
        y = random.randint(1, 99)
        correct_answer = x + y
        op_symbol = "+"
    elif operator_choice == '2':  # 뺄셈
        # 음수가 나오지 않도록 큰 수에서 작은 수를 뺌
        x = random.randint(1, 99)
        y = random.randint(1, 99)
        if x < y:
            x, y = y, x
        correct_answer = x - y
        op_symbol = "-"
    elif operator_choice == '3':  # 곱셈
        x = random.randint(1, 99)
        y = random.randint(1, 99)
        correct_answer = x * y
        op_symbol = "*"
    elif operator_choice == '4':  # 나눗셈
        # 나누는 수 y를 1부터 9 사이, 몫은 1부터 10 사이
        y = random.randint(1, 9)
        quotient = random.randint(1, 10)
        x = y * quotient
        correct_answer = quotient  # 문제: x / y = ?
        op_symbol = "/"

    print(str(n) + ". " + str(x) + " " + op_symbol + " " + str(y) + " = ? ", end="")
    answer = input()

    if answer == "":
        print("입력이 없습니다. 종료합니다.")
        break

    try:
        answer = int(answer)
    except ValueError:
        print("숫자가 아닙니다. 문제를 넘어갑니다.")
        n += 1
        continue

    if answer == correct_answer:
        print("정답입니다.")
        score += 1
    else:
        mistakes += 1
        print("틀렸습니다. 정답은", correct_answer, "입니다.")
        if mistakes >= 3:
            print("틀린 횟수가 3회가 되어 프로그램을 종료합니다.")
            break

    n += 1

print(name, "님이 맞춘 개수는", score, "개 입니다.")
print(name, "님의 맞춘 비율은", score / 10 * 100, "% 입니다.")
print("프로그램을 종료합니다.")
