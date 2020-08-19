def check_winning_candidate(voters, parties):
    lo = 0  # counter
    initial = str()  # previous counter

    hi = 0

    previous_counter = 0  # previous_index counter
    index = 0

    if parties[0] == '-':
        while parties[index] == '-':
            index += 1

        # check is sequence is 'A'

        if parties[index] == 'A':
            lo += index
            initial = 'A'

            previous_counter = index

            lo += 1
            index += 1

    for index in range(voters):

        if parties[index] != '-':

            # check if sequence is B and counter is B

            if initial == 'B' and parties[index] == 'B':

                hi += (index - previous_counter - 1)
                initial = 'B'

                previous_counter = index


            # check if sequence is A and counter is A

            if initial == 'A' and parties[index] == 'A':

                lo += (index - previous_counter - 1)

                initial = 'A'

                previous_counter = index

            if parties[index] == 'A':
                lo += 1

                initial = 'A'
                previous_counter = index

            else:
                hi += 1

                initial = 'B'
                previous_counter = index

    if parties[voters - 1] == '-':

        if initial == 'B':

            hi += (voters - 1 - previous_counter)

    # final winner announcement

    if lo < hi:
        print("B", end="")

    elif lo > hi:
        print("A", end="")
    else:
        print("Coalition government", end='')


def main():
    voters = int(input())
    parties = str(input())
    check_winning_candidate(voters, parties)


if __name__ == '__main__':
    main()
