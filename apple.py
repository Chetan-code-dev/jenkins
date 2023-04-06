def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print the first 10 numbers in the Fibonacci sequence
for i in range(10):
    print(fibonacci(i))
