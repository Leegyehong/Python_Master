# 입력값과 결괏값에 따른 함수 형태

# 일반적 함수
# def 함수 이름(매개변수):
#   수행할 문장
#   ...
#   return 결괏값

def add(a,b):
    result = a + b
    return result # a+b의 결괏값 반환

a = add(3,4)
print(a)

# 입력값과 결괏값이 있는 함수의 사용법
# 결괏값을 받을 변수 = 함수 이름(입력인수1, 입력인수2, ...)