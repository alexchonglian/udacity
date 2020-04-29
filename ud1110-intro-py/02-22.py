verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

answer = """
What is the length of the string variable verse? {}
What is the index of the first occurrence of the word 'and' in verse? {}
What is the index of the last occurrence of the word 'you' in verse? {}
What is the count of occurrences of the word 'you' in the verse? {}
""".format(len(verse), verse.find('and'), verse.rfind('you'), verse.count('you'))

print(answer)

