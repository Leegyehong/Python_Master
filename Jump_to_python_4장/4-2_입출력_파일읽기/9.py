# 파일에 새로운 내용 추가하기
# 쓰기 모드('w')로 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 됩니다.
# 하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있습니다.
# 이런 경우에는 파일을 추가 모드('a')로 열면 됩니다.

f = open("C:/Users/chasu/OneDrive/바탕 화면/Python_Master/새파일.txt", "a")
for i in range(11,20):
    data = "%d 번째 줄입니다. \n" % i
    f.write(data)
f.close()

# 1번째 줄입니다. 
# 2번째 줄입니다. 
# 3번째 줄입니다. 
# 4번째 줄입니다. 
# 5번째 줄입니다. 
# 6번째 줄입니다. 
# 7번째 줄입니다. 
# 8번째 줄입니다. 
# 9번째 줄입니다. 
# 10번째 줄입니다. 
# 11 번째 줄입니다. 
# 12 번째 줄입니다. 
# 13 번째 줄입니다. 
# 14 번째 줄입니다. 
# 15 번째 줄입니다. 
# 16 번째 줄입니다. 
# 17 번째 줄입니다. 
# 18 번째 줄입니다. 
# 19 번째 줄입니다. 