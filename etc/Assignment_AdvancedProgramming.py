#(1번 문제)LAB10-3
## 1(1)
ls = ['a', 'b', 'c', 'd']
def to_upper(char):
    return char.upper()
upper_a_list = list(map(to_upper, ls))
print(upper_a_list)
## 1(2) 람다 활용
upper_a_list = list(map(lambda x: x.upper(), ls))
print(upper_a_list)
## 2(1)
ls = [10, 20, 30]
def twice(value):
    return value*2
def triple(value):
    return value*3
answer = list(map(twice, ls))
print('입력 값의 두 배 :', answer)
answer = list(map(triple, ls))
print('입력 값의 세 배 :', answer)
## 2(2)
answer = list(map(lambda x: x*2, ls))
print('입력 값의 두 배 :', answer)
answer = list(map(lambda x: x*3, ls))
print('입력 값의 세 배 :', answer)


#(2번 문제)LAB10-4
from functools import reduce
## 1
answer = reduce(lambda x, y: x+y, range(1,101))
print('1에서 100까지의 합 :', answer)
## 2
answer = reduce(lambda x, y: x*y, range(1,11))
print('10! =', answer)


#(3번 문제)LAB10-5
## 1
cubic = [i**3 for i in range(1, 11)]
print('cubic =', cubic)
## 2
a = ['welcome', 'to', 'the', 'python', 'world']
first_a = [i[0] for i in a]
print(first_a)


#(4번 문제)LAB10-6
## 1
cubic = [i**3 for i in range(1, 11) if i**3<=500]
print('cubic =', cubic)
## 2
st = 'Hello 1234 Python'
answer = [c for c in st if c.isdigit()]
print(answer)


#(5번 문제)LAB10-7
## 1
class EvenCounter:
    def __init__(self, n=0):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        temp = self.n
        self.n += 2
        return temp
my_even = EvenCounter()
print(my_even.__next__(), end=' ')
print(my_even.__next__(), end=' ')
print(my_even.__next__(), end=' ')
print(my_even.__next__(), end=' ')
print(my_even.__next__())
# 2
my_even = EvenCounter()
for i in my_even:
    if i <= 20:
        print(i, end=' ')
    else:
        break


#(6번 문제)LAB10-8
## 1
txt = 'Welcome to Busan Metropolitan City'
print(txt.split())
## 2
greet = 'Hello,My name is DongMin,Good to see you again'
print(greet.split(','))
##3
fruits = 'Apple|Banana|Melon|Orange'
print(fruits.split('|'))


#(7번 문제)LAB9-6
## 1
class Dog:
    def bark(self):
        print('멍멍~~')
my_dog = Dog()
my_dog.bark()


#(8번 문제)LAB9-7
n = 100
m = 100
if n is m:
    print('n is m')
else:
    print('n is not m')
# 출력 결과: 'n is m'
## 정수 자료형은 불변(immutable)객체로 수정이 불가능하고
## 같은 저장 위치를 참조하므로 n과 m은 같은 값으로 간주된다.


#(9번 문제)LAB9-8
## 1
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1, v2 = Vector2D(30, 40), Vector2D(10, 20)
print(v1 * v2)
print(v1 / v2)
## 2
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(10, 20)
print(-v1)


#(10번 문제)LAB9-9
import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.norm() > other.norm()

    def __ge__(self, other):
        return self.norm() >= other.norm()

    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return "{}".format(self.x, self.y)

v1, v2 = Vector2D(30, 40), Vector2D(10, 20)
print(v1 > v2)
print(v1 >= v2)
print(v1 < v2)
print(v1 <= v2)


#(11번 문제)LAB9-10
## 1
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])
## 2
class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
r1 = Rect(100, 200)
print(r1.__dict__) # 은닉된다
print(r1.__dict__['_Rect__width'])


#(12번 문제)LAB8-1
##11
a = [10, 20, 30]
a[3] # IndexError 발생
n = int('20%') # ValueError 발생
a = 100 + '200' # TypeError 발생


#(13번 문제)LAB8-2
## 1
try:
    10 * (30 / 0)
except ZeroDivisionError:
    print('오류: 0으로 나눔을 시도했습니다.')
## 2
try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError:
    print('오류: 입력값이 정수나 실수가 아닙니다.')
## 3
import sys
try:
    f = open('myfile.txt')
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')


#(14번 문제)LAB8-3
## 1
a = [1, 2, 3, 4, 5,]
try:
    element = int(input('a의 요소를 하나 선택하시오 :'))
    print(element, '은(는)', a.index(element)+1, '번째 요소입니다.')
except ValueError:
    print(element, '은(는) a의 요소가 아닙니다.')
## 2
a = [1, 2, 3, 4, 5,]
try:
    element = int(input('a의 요소를 하나 선택하시오 :'))
    print(element, '은(는)', a.index(element)+1, '번째 요소입니다.')
except ValueError:
    print('입력값이 정수나 실수가 아님')

#(15번 문제)LAB7-1
from datetime import datetime
start_time = datetime.now()r
def print_now():
    XM = '오전'
    start_time = datetime.now()
    Y, M, D = start_time.year, start_time.month, start_time.day
    if start_time.hour > 12:
        XM = '오후'
        h, m, s = start_time.hour - 12, start_time.minute, start_time.second
    print(f'오늘의 날짜 : {Y}년 {M}월 {D}일')
    print(f'현재시간 : {XM} {h}시 {m}분 {s}초')
print_now()
