def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

n = int(input("Enter a number: "))
even_numbers(n)