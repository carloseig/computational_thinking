target = int(input('Choose a number: '))
epsilon = 0.0001
step = epsilon**2 
answer = 0.0

while abs(answer**2 - target) >= epsilon and answer <= target:
    print(abs(answer**2 - target), answer)
    answer += step

if abs(answer**2 - target) >= epsilon:
    print(f'Square root not found {target}.')
else:
    print(f'The square root of {target} is {answer}.')