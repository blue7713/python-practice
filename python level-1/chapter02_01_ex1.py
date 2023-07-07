# print 사용법
# 파이썬 3가지 Print Formatting

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1
ex1 = ('n = %s, s = %s, sum = %d' % (n, text, (x + y)))
print(ex1)

# 출력2
ex2 = ('n = {n}, s = {s}, sum = {sum}'.format(n = n, s = text, sum = x + y))
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

# 구분기호
m = 1000000

print(f'm : {m:,}')
print()

# 정렬 
# ^ : 가운데, < : 왼쪽, > : 오른쪽
t = 20
print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t left : {t:<10}")
print(f"t right : {t:>10}")

print(f"t center : {t:-^10}")
print(f"t center : {t:*<10}")