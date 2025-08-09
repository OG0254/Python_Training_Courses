with open('part21bdata.txt', 'r') as file: # pulls these data from the data.txt created
    # data = file.read() # reads the whole statement
    # print(data)

    # data = file.readline(5) # reads hello
    # print(data)

    data = file.readlines() # reads each line on it's own ['hello\n', 'abc\n', '123']
    print(data)