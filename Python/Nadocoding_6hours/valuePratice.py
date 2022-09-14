# 전역, 지역 변수
import math

value = 100
def inner():
    global value
    value = 200

inner()
print(value)
    ## 내부 스코프에서 전역 변수에 접근하려면 global 변수이름 으로 먼저 쓰겠다고 선언.
    ## 선언 전에 같은 이름을 쓰면 컴파일 에러가 뜸.

def std_weight(height=100, gender="남"):
    weighted = -1

    if(gender == "남자"):
        weighted = 22
    elif(gender == "여자"):
        weighted = 21
    else:
        weighted = 0

    return height, round(math.pow(height/100, 2) * weighted, 2)

#print("키 {}cm 남자의 표준 체중은 {}kg 입니다.".format(std_weight(175, "남자")))
#이건 씨1바 도대체 왜 안 되는지 모르겠다 파이썬 ㅁㅊ새끼
print("키 %icm 남자의 표준 체중은 %fkg 입니다." % std_weight(175, "남자"))