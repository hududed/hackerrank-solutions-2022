def truckTour(petrolpumps):
    firstPoint = reserveFuel = 0
    for i in range(len(petrolpumps)):
        reserveFuel += petrolpumps[i][0] - petrolpumps[i][1]
        if reserveFuel < 0:
            firstPoint = i + 1
            reserveFuel = 0
    return firstPoint


if __name__ == '__main__':
    n = int(input().strip())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    print(truckTour(petrolpumps))
