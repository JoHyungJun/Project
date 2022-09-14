# 리스트 [] (배열)

alphabet = ['a', 'b', 'c', 'e', 'f']
print(alphabet.index('a'), alphabet.count('a'))
    ## string 도 결국 char의 집합이므로 여러 string api를 사용 가능한 듯. find는 안 되네

alphabet.append('g')
alphabet.insert(3, 'd')
alphabet.pop()
print(alphabet)

alphabet.clear()
alphabet = 5
number = [1, 2, 3, 4]
number.append(alphabet)
    ## alphabet을 []로 감싸면 안 된다. 그럼 리스트 안의 리스트라 함수 활용이 불가능해짐.
number.reverse()
print(number)
number.sort()
print(number)
    ## reverse 나 sort는 return 값이 없다. 따라서 그냥 sort하는 용도로만.


# 튜플. Tuple은 수정, 추가 등이 불가하나 속도가 빠른 list이다.

myName = ("조형준")
(myFace, myBody, myCharacter) = ("잘생김", "울끈불끈", "귀여움")
print(myName + "은", myFace, myBody, myCharacter)
    ## 여러 변수를 한 번에 손쉽게 설정 가능하다.