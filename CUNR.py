def calculate_double_factorial(n, mod=10**6):
    result = 1
    for i in range(2 * n - 5, 1, -2):
        result = (result * i) % mod
    return result

n = 743
print(calculate_double_factorial(n))
