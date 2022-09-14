# Set. 집합의 개념이 들어가 있는 자료구조. 중복과 순서가 없다.
# dictionary 와 선언 방식이 똑같으면서 왜 함수에는 차이가 있는지는 모르겠다. 상속인 듯?

faceSet = {"강동원" , "차은우", "조형준", "조형준"}
print(faceSet)
    ## 중복 원소가 있으면 알아서 지우는 듯

cuteSet = set(["박보영", "츄", "조형준"])
    ## set(배열) 의 형태로 자료구조를 바꿀 수 있다. list, tuple, set 도 있다.
    ## type(배열) 함수로 해당 배열이 어떤 클래스인지도 알 수 있다.

print("훈훈하면서 귀여운 사람 :", faceSet & cuteSet)
    # 교집합. faceSet.intersection(cuteSet) 과 같음.

print("훈훈하거나 귀여운 사람 :", faceSet | cuteSet)
    # 합집합. faceSet.union(cuteSet) 과 같음.

print("훈훈하기만 한 깡통 사람 : ", faceSet - cuteSet)
    # 차집합. faceSet.difference(cuteSet) 과 같음.

sunflower = {"김래원", "조직원", "병진이형"}
print(sunflower)
print("병진이형은 나가 뒤지기 싫으면")
sunflower.remove("병진이형")
sunflower.add("\"고맙다.. (절뚝 절뚝)\"")
print(sunflower)