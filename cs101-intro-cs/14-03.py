# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    nums = map(int, list(string))
    maxv, ret, tmp = 0, [], []
    for i in nums:
        if i > maxv:
            if tmp:
                ret.append(tmp)
                tmp = []
            ret.append(i)
            maxv = i
        else:
            tmp.append(i)
    if tmp:ret.append(tmp)
    return ret
            
#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print numbers_in_lists(string)
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print numbers_in_lists(string)
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print numbers_in_lists(string)
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print numbers_in_lists(string)
