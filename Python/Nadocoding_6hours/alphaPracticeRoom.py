from random import *

timeRandList = range(1, 51)
timeRandList = [randint(5, 50) for i in timeRandList]

number = 1
customerCount = 0;
correct = ' '
time = 0;
while True:
    if(number > 50):
        break

    time = timeRandList[number-1]
    if 5 <= time <= 15:
        correct = "O"
        customerCount += 1
    else:
        correct = " "

    print("[%s] %d번째 손님 (소요시간 : %d분)" %(correct, number, time))

    number += 1

print("\n총 탑승 승객 : {}".format(customerCount))
