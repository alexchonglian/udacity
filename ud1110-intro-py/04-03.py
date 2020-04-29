points = 174  # use this input to make your submission

# write your if statement here

if 1 < points < 50:
    prize = 'wooden rabbit'
elif 51 < points < 150:
    pass
elif 151 < points < 180:
    prize = 'wafer-thin mint'
elif 181 < points < 200:
    prize = 'penguin'

if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."
print(result)