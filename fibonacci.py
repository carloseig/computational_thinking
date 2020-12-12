def fibonacci(n):
    """This software calculates the n-th Fibonacci number

    n int > 0
    """
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Type an integer: '))
print(f'The {n}th number of Fibonacci is {fibonacci(n - 1) + fibonacci(n - 2)}')
