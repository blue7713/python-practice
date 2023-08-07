# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서ㅇ, 중복ㅇ, 수정x, 삭제x) # 

# 선언

a = ()
b = (1,) # 원소가 1개일 때는 , 로 끝나야 튜플로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) # 리스트로 형변환

# 수정 x

# d[0] = 1500 # 에러

# 슬라이싱
print('>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3 # 튜플 선언(괄호는 생략 가능), 팩킹
t3 = 4, # 튜플 선언
x1, x2, x3 = t2 # 언팩킹
x4, x5, x6 = 4, 5, 6 # 언팩킹

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)