import  random

num = random.randint(1, 10)
count = 0

while True:
    try:
        my_number = int(input("Enter a number: (1-10)"))
        if my_number == num:
               print("You guessed right!")
               break
        elif my_number > num:
               print("UP!")
        elif my_number < num:
               print("DOWN!")
    except:
        print("Error 발생, 숫자를 입력하세요")
