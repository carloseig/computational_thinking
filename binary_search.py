target = int(input('Choose a number: '))
epsilon = 0.001
low = 0.0
high = max(1.0, target)
answer = (high + low) / 2

while abs(answer**2 - target) >= epsilon:
    print(f'low={low}, high={high}, answer={answer}')
    if answer**2 < target:
        low = answer
    else:
        high = answer

    answer = (high + low) / 2

print(f'The square root of {target} is {answer}.')