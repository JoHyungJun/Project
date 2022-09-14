# 사전. 일종의 자료구조인 듯.

dictionary = {8:"a", "lock":"key"}
print(dictionary["lock"], dictionary.get(8), 100 in dictionary)

del dictionary[8]
    ## index 혹은 key를 삭제

dictionary["Me"] = "You"
print(dictionary.keys(), dictionary.values())
print(dictionary.items())
    ## string과 함께 print를 하면 오류가 난다. dict_values 와 str을 같이 못 쓴대 ㅡㅡ

dictionary.clear()

from random import *
replyList = list(range(1, 21))
shuffle(replyList)
coffee = [replyList[1], replyList[2], replyList[3]]
    ## 애초에 winning = sample(replyList, 4) 했으면 굿
print("-- 당첨자 발표 --\n치킨 당첨자 :", str(replyList[0]) +"\n커피 당첨자 :", coffee)
