## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
i = 0
odd_count = 0
odd_sum = 0

while i < len(num_list) and odd_count < 5:
    if num_list[i] % 2 == 1:
        odd_sum += num_list[i]
        odd_count += 1
    i += 1

print(odd_sum)    
