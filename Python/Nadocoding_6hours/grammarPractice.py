# if문
myAge = int(input("나이를 입력해주세요 : "))
if myAge == 28 or myAge == 95:
    print("동갑내기 친구네!")
elif 100 >= myAge > 28:
    print("어우 반갑습니다 안녕하세요")
else:
    print("어린너무쉐끼가,, 라뗴는 말여,,")

    ## 데이터타입이 맞지 않으면 에러.
    ## for문의 조건이 and인 경우 num1 <= value <= num2 로 해도 된다.


# for문
index = -999
for index in reversed(range(5)):
    print("당신의 목숨 카운트다운.. %d" %(index))
    if index > 0:
        continue

    ## for문의 활용
    array = [1, 2, 3]
    array = [i*100 for i in array]
    print(array)
    ## array 에 있는 i 를 꺼내서 대괄호 맨 앞에 값을 넣겠다.

# while문
index = 5
while index > 0:
    print("다시 기회를 주겠다.. {}".format(index))
    index-=1
print(" - 끝 -.")
    ## 들여쓰기에 따라 while문인지 while문을 빠져나온 코드인지 구분함.
    ## 무한루프는 Ctrl c 로 빠져나오기, 강제종료.

while True:
    wtf = input("오빠 나 오늘 달라진 거 없어?")
    if(wtf == "오늘 생기있는 입생로랑 19호 공주의 매트레드 컬러감으로 화사함을 한껏 올렸네? 예쁘다"):
        print("으음! 역시 오빠가 짱이얌 >_<!")
        break
    elif(wtf == "살이 쪘나?"):
        print("당신은 피살되었습니다.\ndead end -.")
        break
    else:
        print("ㅎㅎ 한번 더 기회를 줄게?")
        continue