def truckTour(petrolpumps):
    start, tank = 0, 0
    for i in range(len(petrolpumps)):
        # since 1 km == 1l, we assume gas_used == gas_received
        gas_received, distance = petrolpumps[i]
        tank += gas_received - gas_used
        if tank < 0:
            start = i + 1
            tank = 0
    return start


if __name__ == '__main__':
    n = int(input().strip())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    print(truckTour(petrolpumps))
