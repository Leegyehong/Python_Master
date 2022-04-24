# enumerate, 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# for문에서 함께 쓰면 자료형의 현재 순서, 인덱스 값을 쉽게 알 수 있다.