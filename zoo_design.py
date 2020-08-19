from sys import maxsize


def getCheapestIndex(costPerMeter):
    if costPerMeter[0] <= costPerMeter[1] and costPerMeter[0] <= costPerMeter[2]:
        return 0
    elif costPerMeter[1] <= costPerMeter[2] and costPerMeter[1] <= costPerMeter[0]:
        return 1
    else:
        return 2


def get_output():
    costPerMeter = list(map(int, input().split()))

    maxArea = list(map(int, input().split()))
    value1 = list(map(int, input().split()))
    value2 = list(map(int, input().split()))
    value3 = list(map(int, input().split()))
    val = []
    val.append(value1[0])
    val.append(value2[0])
    val.append(value3[0])
    area = []
    area.append(value1[1])
    area.append(value2[1])
    area.append(value3[1])

    total_area = int(input())

    totalAreaLeft = total_area - (val[0] * area[0] + val[1] * area[1] + val[2] * area[2])
    cost = 0

    cost += val[0] * area[0] * costPerMeter[0] + val[1] * area[1] * costPerMeter[1] + val[2] * area[2] * costPerMeter[2]

    areaLeft = [maxArea[0] - (val[0] * area[0]), maxArea[1] - (val[1] * area[1]),
                maxArea[2] - (val[2] * area[2])]

    while (totalAreaLeft > 0):
        indexOfCheapest = getCheapestIndex(costPerMeter)
        areaUsed = min(totalAreaLeft, areaLeft[indexOfCheapest])

        cost += areaUsed * costPerMeter[indexOfCheapest]
        totalAreaLeft -= areaUsed
        areaLeft[indexOfCheapest] -= areaUsed

        costPerMeter[indexOfCheapest] = maxsize
    return cost


if __name__ == '__main__':
    print(get_output(), end='')
