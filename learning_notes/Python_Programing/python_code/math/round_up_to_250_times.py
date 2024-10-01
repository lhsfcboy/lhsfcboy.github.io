def round_to_250_times(number):
    return number + 250 - number % 250


if __name__ == '__main__':
    for num in [1008875, 1007527, 1006894, 1005743, 1004712]:
        print(round_to_250_times(num))