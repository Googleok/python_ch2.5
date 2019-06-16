
def dummy():
    pass

def my_function():
    print('Hello World')

def times(a, b):
    return a * b

def none():
    return

def my_function2(func):
    func()

dummy()
my_function()
times(10, 20)
print(none())

# 함수도 객체다.
print(dummy, type(dummy))
f = my_function
f()
my_function2(f)

print(f, my_function)

# 여러 return 값
def func():
    return 10, 'hello', {1, 2, 3}, (1, 2, 3)

n, s, s2, t = func()
print(n, s, s2, t)

