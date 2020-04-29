names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ', '_')

print(usernames)


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token.startswith('<') and token.endswith('>'):
        count += 1

print(count)


items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
html_str = "<ul>\n" + "".join(["<li>{}</li>\n".format(item) for item in items]) + "</ul>"



print(html_str)