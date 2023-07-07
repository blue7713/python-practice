# print 사용법

# 기본 출력
print("Python Start!")
print('Python Start!')
print('''Python Start!''')
print("""Python Start!""")
print()

# separator 옵션 : 삽입하여 나눠 줄 문구 지정
print('P', 'Y', 'T', 'H', 'O', 'N', sep=' ')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')
print()

# end 옵션 : 마지막에 어떻게 할 지 지정, end 옵션이 들어가면 줄바꿈 x
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션 # 지정된 파일에 내용을 적음
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 정수, s : 문자열, f : 실수형)
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', '2'))
print('{1} {0}'.format('one', '2'))
print()

# %s
print('%10s' % ('nice1111')) # 총 자리수 10개, 나머지 공백처리, 오른쪽에서 채움
print('{:>10}'.format('nice'))

print('%-10s' % ('nice1111')) # 총 자리수 10개, 나머지 공백처리, 왼쪽에서 채움
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) # 공백 대신 _로 채움
print('{:^10}'.format('nice')) # 중앙정렬

print('%.5s' % ('nice')) # 5글자만 출력
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy')) # 자리수 10개 중 5개만 출력
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42)) # 총 자리수 4개, 나머지 공백처리, 오른쪾부터 채움
print('{:4d}'.format(42))
print()

# %f
print('%f' % (3.143434343434))
print('{:f}'.format(3.143434343434)) 

print('%06.2f' % (3.141592653589793)) # 총 6자리, 소수 2자리(정수부.소수부)
print('{:06.2f}'.format(3.141592653589793)) # 소수점도 1자리로 취급
print()