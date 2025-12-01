# Get the total count of number listed in the dictionary which is multiple of
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

multiples_count = {i: sum(num % i == 0 for num in numbers) for i in range(1, 10)}

print(multiples_count)
