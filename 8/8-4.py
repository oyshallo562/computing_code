def sum(x,y) :
    return x + y

def sub(x,y) :
    return x - y

def mul(x,y) :
    return x * y

def div(x,y) :
    return x / y

def calc(x,y,op):
    if op == '+':
        return sum(x,y)
    elif op == '-':
        return sub(x,y)
    elif op == '*':
        return mul(x,y)
    elif op == '/':
        return div(x,y)
    else:
        print("잘못된 연산자입니다.")
        return None

print(calc(3,4,'+'))