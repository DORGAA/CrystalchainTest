def max_diff(int_array):

    data = []
    for i, value in enumerate(int_array):
        seq = int_array[:i]
        if seq:
            a = max(list(map(lambda x: value - x, seq)))
            data.append(a)

    return max(data)


print(max_diff([100, 10, 5, 10, 1, 8, 16, 21]))


