import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 1. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a name:').upper()
result = [phonetic_dict[letter] for letter in word]
print(result)

