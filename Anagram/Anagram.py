def main(firstword, secondword):
  firstword = sorted(firstword.lower())
  secondword = sorted(secondword.lower())
  index = 0

  for letter in firstword:
    if letter != secondword[index]:
      return "These two words are not anagrams"
    elif len(firstword) - 1 == index:
    	return "These two words are anagrams"
    index += 1

print(main("Listen", "Silent"))
print(main("evil", "Vile"))
print(main("Drive", "dave"))