# 기본 인수값
def incr(a, step=1):
    return a + step

# 오류
# def decr(step=1, a):
#     return a + step
# decr(10)


print(incr(10))
print(incr(10, step=2))
print(incr(10, 4))

# 키워드 인수
def area(width, height):
    return width * height


print(area(10, 20))
print(area(width=10,height=20))
print(area(height=20, width=10))

# 오류
# area(20, width=10)
# area(height=20, 10)

# 가변인수
def vargs(a, *args):
    print(a, args)


vargs(10)
vargs(10, 1)
vargs(10, 1, 2, 3, 4, 5)

def _print(*args, end='newline'):
    print(args, end)

_print(10, 20, 30)
_print(10, end='tab')
_print(10, 'tab')

# c의 printf 흉내내기
def printf(format, *args):
    print(format % args)


# printf("%s이 %d원짜리 %s를 입고 %s을 차고 노래를 한다.", "타잔, 100, 티, 칼")

# 정의되지 않은 키워드 인수 처리하기
def f(width, height, **kw):
    print(width, height)
    print(kw)


f(10, 20)
f(10, 20, depth=10)
f(10, 20, depth=10, dimension=3)
# 에러
# f(10, 20, depth=30, 40)

def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)


g(10, 20)
g(10, 20, 30)
g(10, 20, c=60)
g(10, 20, 30, 40, c=60, d=70)

# 튜플/사전 파라미터
def h(name, age, height):
    print(name, age, height)


h('둘리', 10, 150)

t = ('둘리', 10, 50)
h(t[0], t[1], t[2])
h(*t)

d = {'name': '둘리', 'age':10, 'height': 150}
h(d['name'], d['age'], d['height'])
h(**d)
