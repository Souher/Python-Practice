from itertools import count
from operator import le


def compress_string(letters):
  if len(letters) == 0:
    return 'no letters to compress'
  elif len(letters) == 1:
    print('{letters}1'.format(letters))
  else:
    compressed_letters = ''

    for letter in get_unique_letters(letters):
      count = letters.count(letter)
      compressed_letters = compressed_letters + letter + str(count)
  print(compressed_letters)
      

def get_unique_letters(letters):
  unique_letters = ''
  for letter in letters:
    if letter not in unique_letters:
      unique_letters = unique_letters + letter
  return unique_letters

compress_string("abbcccdddd")

### Decompress ###

def decompress_string(letters):
  list_of_letters = list(letters)
  decompress_letters = ''

  while len(list_of_letters) > 0:
    letter = list_of_letters[0]
    count = int(list_of_letters[1])

    while count > 0:
      decompress_letters = decompress_letters + letter
      count -= 1
    
    decompress_letters = decompress_letters + ' '
    
    list_of_letters.pop(0)
    list_of_letters.pop(0)
    
  
  print(decompress_letters)

decompress_string('a1b2c3d4')
