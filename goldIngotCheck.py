def get_max_bar(values):
    if values is None:
        return 0

    st = [-1]

    maximum_volume = 0

    for index, vals in enumerate(values + [-1]):
        while st and st[-1] >= 0 and vals <= values[st[-1]]:
            maximum_volume = max(values[st.pop()] * (index - st[-1] - 1), maximum_volume)

        st.append(index)

    return int(maximum_volume)


def get_largest_ingot(values, vol, l, h):
    simple_volume = vol * l * h

    largest_volume = sum(values) * int(l) * int(h)
    mod = (10 ** 9) + 7

    return int(largest_volume - simple_volume) % mod


def main():
    num_gold_ingots = int(input())
    dim = list(map(int, input().split()))
    breadth = dim[0]
    height = dim[1]
    bars = list(map(int, input().split()))
    m = get_max_bar(bars)
    print(int(get_largest_ingot(bars, m, breadth, height)),end='')


if __name__ == '__main__':
    main()