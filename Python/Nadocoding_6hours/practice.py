# 주석은 # 으로.
''' 작은 따옴표 3개로 여러 줄의 주석 가능. '''
# 여러 문장 주석처리는 스크롤 긁고 ( Ctrl + / )


# 콘솔 프린트 명령어
print(8)
print(8, \
    8)
    ## 줄 구분을 하려면 역슬러쉬를 치고 엔터를 치면 두 줄은 한 문장으로 취급.


# Boolean
# - True, False 의 값이 출력 됨. 소문자 대문자 주의.
print(5>=10)


# 변수
myName = '조형준'
age = 28
isMale = True
isHeHandsome = True
print("제 이름은 " + myName + "\n제 나이는 " + str(age) + "\n저는 남자일까요? : " + str(isMale))
    ## 문자열 이외의 자료형은 string으로 묶을 때 꼭 str을 써줘야하나보다.
print("저는 잘생겼을까요? :", isHeHandsome)
    ## 이런 식으로 str() 과 + 연산자를 같이 쓰는 방식 말고 , 를 사용할 수도 있다. 한칸은 자동으로 띄어짐.


# 연산자
print(2**3)
    ## 제곱 표현.
print(10//3 , 10%3)
    ## 각각 몫, 나머지 표현.
print((not(True)), True and False, False or True)
    ## ! 연산자는 없음. & 와 | 연산자는 있다.
    ## | 와 & 도 정상 작동이 안 된다. 다른 의미인 듯.


# 숫자처리함수
print(abs(-8), pow(2, 3), max(0, 8), min(8, 80), round(8.499))

from math import *
print(floor(8.999), ceil(7.001), int(sqrt(64)))

from random import *
print('이번주 행운의 로또는 ~~~~~>', (int(random() * 45) + 1))
print('뽀너스 숫자는 ~~~~~~~~~~~>', randrange(1, 46))
    ## 앞 이상, 뒤 미만
print('주작 아니야 다시 뽑을게 ~~~>', randint(1, 45))
    ## 앞 이상, 뒤 이하
