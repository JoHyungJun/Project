# 함수 선언 및 활용법
def myFunction(name="이름 없음", age=0):
    print("제 이름은 {}이고, 나이는 {}살 입니다.".format(name, age))
    return 2022 - age + 1, "잘생김"
    ## 함수 선언법 유의. 파이썬은 함수의 내부 영역 구분을 들여쓰기로 한다.
    ## return 값을 콤마로 구분하여 여러개를 내보낼 수 있다.
    ## 이렇게 콤마로 구분된 값들을 튜플이라 하며, 일반 변수로 받을 때는 똑같이 콤마로 구분해서 받을 수 있음.
    ## 파라미터의 기본값은, 만약 파라미터가 들어오지 않으면 저 값을 사용함.

print("제가 태어난 년도는 %i년 입니다. 제 얼굴은 %s" % myFunction("조형준", 28))
print("응애 전 아직 이름이 없어요.", myFunction(age=1), end=" ")
    ## 이렇게 파라미터의 특정 변수만 값을 넣고 사용할 수 있고, 이때는 변수의 순서와 상관 없다.
    ## 프린트 함수는 기본적으로 println이고, 다음 줄에 바로 적고 싶다면 end=" "를 써주면 줄 이어서 출력.


# 가변 인자 = 파라메터에 몇 개의 인자가 오는지 몰라
def countNum(*numbers):
    for num in numbers:
        print(num, " ", end=" ")

countNum(1, 2, 3)
countNum(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)