# 리스트 관련 함수

## append
a = [1, 2, 3]
a.append(4)
print(a)
a.append(None)
print(a)
a.append([6,7])
print(a)

## sort
a = [1, 3, 5, 2, 9]
a.sort()
print(a)

## reverse
a = ['a', 'z', 'b']
a.reverse()
print(a)

## index
a = [1, 2, 3]
print(a.index(3))

## insert
a.insert(0,4)
print(a)
a.insert(-1, 99)
print(a)

## remove
a = [1,2,3,1,2,3,]
a.remove(3)
print(a)

a = [1,2,3,4,4,4,4,4]
for i in range(len(a)):
    a.remove(4)
    if not 4 in a:
        break
print(a)

## pop
a= [1,2,3]
a.pop()
print(a)

## count
a = [1, 2, 3, 1,1,1,1,1]
print(a.count(1))

## extend
a = [1, 2, 3]
a.extend([4,5])
print(a)
