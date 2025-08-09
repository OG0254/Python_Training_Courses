import pickle

# phonebook = {
#    'a' : '1',
#    'b' : '2',
#    'c' : '3'
#}

#with open('phonebook.dat', 'wb') as bin:
#    pickle.dump(phonebook, bin) # dump is to write (wb)

#with open('phonebook.dat', 'rb') as bin:
#    data = pickle.load(bin) # load is to read (rb)
#    print(data)

with open('phonebook.dat', 'rb') as bin:
    data = pickle.load(bin) # load is to read (rb)
    print(type(data)) # shows which class it is in that is <class 'dict'> because of the {}

