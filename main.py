start = int(input('start -> '))
end = int(input('end -> '))
for i in range(1, 11):
    for j in range(start, end+1):
        print(f'{j} * {i} = {i*j}', end = '\t\t')
    print()