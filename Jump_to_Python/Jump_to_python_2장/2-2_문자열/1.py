str1 = "Python is very 'fun'"
str2 = "python is very \"fun\""
print(str1) # Python is very 'fun'
print(str2) # Python is very "fun"

multiline = "Life is too short\nYou need python"
multiline2 = """
    Life is too short
    You need python
"""
print(multiline)
print(multiline2)

a = "Life is too short, You need python"
a[3] # 'e'
a[-1] # 'n'
a[0:4] # 'Life

want = 'I want to eat %s apples.' %3
print(want)

eat = 'I want to eat %s apples.' %"three"
print(eat)

percent = "Error is %d%%" %100
print(percent)

style = 'I eat {0} apples.'.format('five')
print(style)

style1 = 'I eat {0} apples.'.format(5)
print(style1)

style2 = 'I eat {0} apples. so I was sick for {1} days'.format(5, 2)
print(style2)

name = '이계홍'
age = 25
print(f'제 이름은 {name}이고, 나이는 {age}입니다.')

dic = {'name' : '이계홍', 'age' : 25}
print(f'제 이름은 {dic["name"]}이고, 나이는 {dic["age"]}입니다.')