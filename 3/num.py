import random

number = random.randint(1, 1000)
count = 1

while True:
    my_number = int(input("숫자를 맞춰보세요(1~1000): "))
    if my_number == number:
        print("정답입니다.")
        print(count, "번 만에 맞추셨습니다.")
        break
    elif my_number < number:
        print("UP")
    else:
        print("DOWN")
    count += 1