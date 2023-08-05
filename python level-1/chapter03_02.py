# Chapter 03_2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드
\n : 줄 바꿈
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""
# I'm Boy

print('I\'m Boy')  # 'm을 출력하는 방법
print('a \t b')  # tab
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Row String
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력, \를 입력하여 다음줄의 모든 주석문을 출력
multi_str = \
    '''
String
Multi Line
Test
'''

print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())  # 첫 문자를 대문자로
print("endswitch?: ", str_o2.endswith("!"))  # 마지막 문자가 !로 끝났는지
print("replace :", str_o1.replace("thon", 'Good'))  # thon을 Good로 교체
print("sorted :", sorted(str_o1))  # 문자열의 정렬하여 리스트로 반환
print("split : ", str_o4.split(' '))  # 공백으로 분리

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  # _iter_ 반복이 가능하다는 의미

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))

# 슬라이싱 연습
print(str_s1[0:3])  # 0 1 2
print(str_s1[5:])  # 5번째부터 끝까지
print(str_s1[:len(str_s1)])  # str_s1[:11]
print(str_s1[:len(str_s1)-1])  # str_s1[:10]
print(str_s1[1:9:2])  # 1부터 8까지 2씩, 1 3 5 7
print(str_s1[-5:])  # 오른쪽에서 5번째부터 끝까지
print(str_s1[1:-2])  # 1부터 -2까지
print(str_s1[::2])  # 처음부터 끝까지 2의 간격으로 출력
print(str_s1[::-1])  # 처음부터 끝까지 오른쪽에서부터 역으로 출력

# 아스키 코드
a = 'z'

print(ord(a))  # 아스키 코드값
print(chr(122))  # 아스키 코드의 문자값
