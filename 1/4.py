#계산기

a = int(input())
b = int(input())
print("원하는 연산 숫자로 입력 : 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈")
c = int(input())
print("-------------------")

if c == 1:
    print("덧셈 결과 : ", a+b)
elif c == 2:
    print("뺄셈 결과 : ", a-b)
elif c == 3:
    print("곱셈 결과 : ", a*b)
elif c == 4:
    print("나눗셈 결과 : ", a/b)
else:
    print("잘못된 입력입니다.")