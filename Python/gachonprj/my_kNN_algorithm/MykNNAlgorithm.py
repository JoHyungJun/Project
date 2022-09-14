import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import numpy as np
import cv2
from random import *
import math


# plt의 title 한글 깨짐 해결 위한 폰트 설정.
rc('font', family='HCR Dotum')


# 사이클마다 그 당시의 평균점의 x, y 좌표. 최초에는 랜덤한 두 좌표로 선정.
averageDotList = [[0, 0], [0, 0]]
colorList = ['red', 'blue']
# sumList는 두 색깔 별로 x좌표 전체합, y좌표 전체합, 점들의 총 카운트 개수, 색깔 순서로 이루어진다.
sumList = [[0, 0, 0, 'red'], [0, 0, 0, 'blue']]


# 앞으로 사용하기 위한 산점도 선언
randomDF = pd.DataFrame()


# 산점도의 초기화. 랜덤값을 100개 넣어줌.
index = 0
randomDF = pd.DataFrame(columns=['x', 'y', 'color'])
while True:
    if index >= 100:
        break

    x = randint(1, 100)
    y = randint(1, 100)
    randomDF.loc[index] = [x, y, 'black']
    index += 1


# 산점도 랜덤 두 점 잡기. 이 과정은 초기 한 번만 쓰임.
for i in range(2):
    tempIndex = -1
    while(True):
        randomIndex = randint(0, 99)
        if(randomIndex == tempIndex):
            continue
        else:
            tempIndex = randomIndex
            break

    randomDF.loc[randomIndex, ['color']] = colorList[i]
    averageDotList[i][0] = int(randomDF.loc[randomIndex, ['x']])
    averageDotList[i][1] = int(randomDF.loc[randomIndex, ['y']])


# 거리값을 계산하는 함수 정의.
# 두 점을 받아 계산 후 앞 점이 가까우면 0, 아니면 1 리턴. 그 값으로 averageDotList의 인덱스 접근 할 것.
def compareDistane(tempList):
    tempDistance = [0, 0]

    # 직선의 방정식 계산. 편의를 위해 굳이 루트를 씌우진 않았다.
    for i in range(2):
        tempDistance[i] = math.pow(averageDotList[i][0] - tempList[0], 2) + math.pow(averageDotList[i][1] - tempList[1], 2)

    if tempDistance[0] >= tempDistance[1]:
        nearestDot = 1
    else:
        nearestDot = 0

    return nearestDot


# 이전 평균점과, 계산 후 새로운 평균점이 같은지 판단하고 같을 때까지 while문 반복.
cycle = 0;
while(True):
    cycle += 1
    isLast = False

    # randomDF를 처음부터 돌면서, 각 점을 compareDistane 함수로 두 점보다 가까운 점을 판별한 후에 그에 맞는 색으로 색칠해준다.
    for i in range(100):
        tempList = randomDF.loc[i, ['x', 'y']]
        nearestIndex = compareDistane(tempList)
        randomDF.loc[i, 'color'] = colorList[nearestIndex]

        for j in range(2):
            sumList[nearestIndex][j] += tempList[j]
        sumList[nearestIndex][2] += 1


    # 평균점 계산
    tempAverageDotList = [[-1, -1], [-1, -1]]
    for i in range(2):
        tempAverageDotList[i][0] = sumList[i][0] / sumList[i][2]
        tempAverageDotList[i][1] = sumList[i][1] / sumList[i][2]

    print("Red 점 개수 : " + str(sumList[0][2]) + '   Blue 점 개수 : ' + str(sumList[1][2]))

    if tempAverageDotList == averageDotList:
        isLast = True   # 여기서 break 걸어주는 게 맞는데 그래프를 보는 편의를 위해 flag로 뒤에서 브레이크 걸어주었다.
    else:
        averageDotList = tempAverageDotList

        for i in range(2):
            for j in range(3):
                sumList[i][j] = 0


    # 매 사이클마다 산점도 출력 반복.
    plt.scatter(randomDF['x'], randomDF['y'], color=randomDF['color'])

    title = ''
    if isLast:
        title = '[마지막] ' + str(cycle) + ' 번 째 사이클'
    else:
        title = str(cycle) + ' 번 째 사이클'

    plt.title(title)
    plt.show()


    if isLast:
        break