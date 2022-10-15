try:
    for i in range(1, 10):
        for j in range(1, 10 + 1):
            print(f'{j} * {i} = {i * j}', end='\t\t')
        print()
except Exception as ex:
    print(ex)