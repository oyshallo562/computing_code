import random

n = 1
score = 0

print("문제를 시작하려면 Enter키를 치세요")
input()

print("이름입력 -> ", end="")
name = input()

print("문제를 10개 풀고 Enter키를 치세요")
input()

while n <= 10:
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    print(str(n) + ". " + str(x) + " + " + str(y) + " = ? ", end="")
    answer = input()

    if answer == "":
        print("입력이 없습니다. 종료합니다.")
        break

    answer = int(answer)

    if answer == (x + y):
        print("정답입니다.")
        score = score + 1
    else:
        print("틀렸습니다.")

    n = n + 1

print(name, "님이 맞춘 개수는", score, "개 입니다.")
print(name, "님의 맞춘 비율은", score/10 * 100, "% 입니다.")
print("프로그램을 종료합니다.")
