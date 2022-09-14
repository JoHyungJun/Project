# String
# - 문자열은 '', "" 다 가능. 연산도 가능.


print('hello', "HELLO")
    ## print(sdasd) : not defined error
print('ha ' * 8)
    ## 단 print('string' + 1 )같은 연산은 안 되나보다.


happyStr = """      웃으면
     복이
     와요 ^^
"""
print(happyStr)
    ## 쓴 그대로 출력이 된다 (공백, 줄나눔 포함) 고로 빈 칸은 다 spcae(' ') 처리.
hoxy = '''
    이것도 된다고?
'''
print(hoxy)
    ## 주석 표시인데 이것도 되네;;

# Silce
chittychittybangbang = '내 이름은 이효리 거꾸로해도 이효리'
name = chittychittybangbang[6:9]
    ## 뒷숫자 직전 인덱스까지
reverseName = chittychittybangbang[-4:]
    ## 마찬가지로 뒷숫자 바로 앞 인덱스까지. 0 대신 :만 써도 ㅇㅋ.
print(name, reverseName)


# 문자열 처리 함수
alphabet = "AbCdEfGhIjKlMnOp"
print(alphabet.lower(), alphabet.upper())
    ## alphabet[0].isUpper() isLower() 함수도 있다. boolean return.
print('길이 :', len(alphabet))
print(alphabet.replace('GhIjKlMnOp', 'uck'),
      alphabet.index("G", 0), alphabet.find("G"),
      alphabet.count('A'))


# 문자열 포맷
print("%d살 때부터 %s를 %c어." % (5, "피아노", '쳤'))
    ## 문법 주의
print("{0}{2}였{1} - {singer}".format("영", "지", "재", singer="창모"))
    ## 그냥 순서대로 쓸 때는 숫자 없이 빈칸으로만.
    ## 변수 singer을 문장 밖에서 먼저 선언했다면 " 앞에 f 를 추가하고 바로 {singer} 사용 가능 (파이썬 3.6v 이상)


# 탈출 문자
print('인생을\r컴공학\b "탈!! 출!!\' \t \\(^0^)\n')


url = 'http://youtube.com'
url = url.replace('http://', '')
url = url[: url.index('.')]
print(url[0:3] + str(len(url)) + str(url.count('e')) + "!")