amount = int(input())
counter = 0
if amount > counter:
    print('+', end='')
    while counter < amount:
        print(f"-+\n{' ' * (counter * 2)}| |\n{' ' * (counter * 2)}+-+", end='')
        counter += 1