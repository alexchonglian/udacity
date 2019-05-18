# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = text.lower()
    lentext = len(text)
    maxl = 0; idx = (0,0)
    for center in range(lentext):
        i,j = center-1, center+1
        while i>=0 and j<lentext and text[i] == text[j]:
            i -= 1;j += 1
        if j-i > maxl:
            maxl = j-i
            idx = (i+1, j)
    for center in range(lentext):
        i,j = center-1, center
        while i>=0 and j<lentext and text[i] == text[j]:
            i -= 1;j += 1
        if j-i > maxl:
            maxl = j-i
            idx = (i+1, j)
    return idx


    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()