# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
count = 140
for line in headlines:
    line += ' '
    if len(line) > count:
        news_ticker += line[:count]
        break
    else:
        news_ticker += line
        count -= len(line)

print(len(news_ticker))
print(news_ticker)