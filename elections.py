def check_single_permutation(num_vehicles):
    initial_permutation = 1
    initial_group = 0

    for vehicle in range(1, num_vehicles + 1):
        initial_permutation *= vehicle
        increment = 1
        for counter in range(1, vehicle + 1):
            increment *= ++counter
            initial_group += (initial_permutation / increment)

    if num_vehicles % 2 == 0:
        initial_group = initial_group - 1

    initial_group = initial_group - num_vehicles
    answer = initial_group / initial_permutation
    answer_rounded = round(answer, 6)
    print(answer_rounded, end="")


def main():
    num_vehicles = int(input())
    speed_arr = list(map(int, input().split()))
    check_single_permutation(num_vehicles)


if __name__ == '__main__':
    main()
