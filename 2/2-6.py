money = int(input("투입한 돈 : "))
price = int(input("커피 값 : "))

change = money - price

c1000 = change // 1000
change = change % 1000

c500 = change // 500
change = change % 500

c100 = change // 100
change = change % 100

c50 = change // 50
change = change % 50

c10 = change // 10

print(f"거스름돈 : {money-price}")
print(f"1000원 지폐 : {c1000}장")
print(f"500원 동전 : {c500}개")
print(f"100원 동전 : {c100}개")
print(f"50원 동전 : {c50}개")
print(f"10원 동전 : {c10}개")