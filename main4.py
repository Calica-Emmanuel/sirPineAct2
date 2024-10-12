numbers = (1, 3, 2, 4, 3, 1, 2, 5)
counted_numbers = {}

for num in numbers:
    if num in counted_numbers:
        counted_numbers[num] += 1
    else:
        counted_numbers[num] = 1

print("Numbers that appear more than once:")
for num in counted_numbers:
    if counted_numbers[num] > 1:
        print(num)
