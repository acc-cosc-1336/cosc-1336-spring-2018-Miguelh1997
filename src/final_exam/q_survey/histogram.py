def display_histogram(values):

    for value in values:
        i = 0
        print(value, end=' ')
        while i < value:
            print('*', end=' ')

            i += 1

        print()

    print()
