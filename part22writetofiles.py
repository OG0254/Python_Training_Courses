userInput = input('Enter your suggestion here : ')

# with open('part22bdata.txt', 'w') as file: # 'w' writes to files
    # file.write(userInput + '\n')

with open('part22bdata.txt', 'a') as file: # 'a' appends to files without removing what was initialy there
    file.write(userInput + '\n')