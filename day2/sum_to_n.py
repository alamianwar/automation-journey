def sum_to_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter a number: "))

print(f"The sum from 1 to {n} is {sum_to_n(n)}")