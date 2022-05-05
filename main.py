#student_dict = {
#    "student": ["Björn", "Jiaqi", "Anders"],
#    "score": [56, 99, 13]
#}

#Looping through dictionaries:
# for (key, value) in student_dict.items()
#   print(value)


#student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#Loop through a daa frame
#for (key, value) in student_data_frame.items():
#   print(value)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
#    if row.student == "Björn":
#        print(row.score)

#{new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dict in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)
alpha = True

while alpha:
    #TODO 2. Create a list of the phonetic code words from word that the user inputs
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        print("Sorry, only letters!")
    else:
        print(output)

