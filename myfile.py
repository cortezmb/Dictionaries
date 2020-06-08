import pickle

phonebook_dict = {'Alice': '(703) 493-1834',
'Bob': '(857) 384-1234',
'Elizabeth': '(484) 584-2923'}

# you need to load data into dictionary before asking what user wants to do
with open('phonebook.pickle', 'wb') as fh:
    #Not sure why I used dump function instead of load. Need to ask DiR
    pickle.dump(phonebook_dict, fh)
    #you can access keys and values in the this dictionary
    # print(data["name"])