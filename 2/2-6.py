money = int(input("투입한 돈 : "))
price = int(input("커피 값 : "))

change = money - price

c1000 = change // 1000
change = change % 1000

c500 = change // 500
change = change % 500

c100 = change // 100

print(f"거스름돈 : {money-price}")
print(f"1000원 지폐 : {c1000}장")
print(f"500원 동전 : {c500}개")
print(f"100원 동전 : {c100}개")