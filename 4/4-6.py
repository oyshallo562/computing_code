import  random

num = random.randint(1, 10)
count = 0

while True:
   my_number = int(input("Enter a number: (1-10)"))
   if my_number == num:
       print("You guessed right!")
       break
   elif my_number > num:
       print("DOWN!")
   elif my_number < num:
       print("UP!")
