# 문자 개수 세기(count)
a = "Hello Python"
print( a.count('o'))

#위치 알려주기(find)
b = "Hello Python"
print(b.find('o'))
print(b.find('A'))

# 문자열 삽입(join)
print("/".join('abcd')) #abcd 문자열의 각각의 문자 사이에 를 삽입

# 소문자를 대문자로 바꾸기(upper)
c = "Hello Python"
print(c.upper())

# 대문자를 소문자로 바꾸기(lower)
print(c.lower())

#왼쪽 공백 지우기(Istrip)
d="           Hello Python"
print(d.lstrip())

#오른쪽 공백 지우기(rstrip)
e = "Hello Python           "
print(e.rstrip)

#양쪽 공백 지우기(strip)
f=(" Hello Python ")
print(f.strip())

# 문자열 바꾸기(replace)
g = " Hello Python"
print(g.replace("Python", "Al"))

# 문자열 나누기(split)
h = "Hello Python"
print(h.split())