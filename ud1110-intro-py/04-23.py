start_num = 1 #provide some start number
end_num = 10  #provide some end number that you stop when you hit
count_by = 2  #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
i = start_num
while i < end_num:
    i += count_by
    
break_num = i

print(break_num)



start_num = 1 #provide some start number
end_num = 10  #provide some end number that you stop when you hit
count_by = 2  #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    i = start_num
    while i < end_num:
        i += count_by
    result = i
    
break_num = i

print(result)





limit = 40

# write your while loop here
i = 0
while i*i < limit:
    nearest_square = i*i
    i += 1

print(nearest_square)