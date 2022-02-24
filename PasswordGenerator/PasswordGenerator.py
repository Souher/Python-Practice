import string
import random

def random_numbers(amount_of_numbers):
  numbers = []
  for x in range(amount_of_numbers):
    numbers.append(random.choice(string.digits))
  return numbers

def random_punctuation(amount_of_punctuation):
  punctuation = []
  for x in range(amount_of_punctuation):
    punctuation.append(random.choice(string.punctuation))
  return punctuation

def random_letters(amount_of_letters):
  letters = []
  for x in range(amount_of_letters):
    letters.append(random.choice(string.ascii_letters))
  return letters

def password_randomiser(letters, numbers, punctuation):
  password_list = []
  temp_password = []

  for x in letters:
    temp_password.append(x)
  for x in numbers:
    temp_password.append(x)
  for x in punctuation:
    temp_password.append(x)
  
  while len(temp_password) > 0:
    temp_choice = (random.choice(temp_password))
    password_list.append(temp_choice)
    temp_password.remove(temp_choice)

  password = "".join(password_list)
  return password

def main():
  is_valid_choice = False
  length_choice = [8, 9, 10, 11, 12]

  while is_valid_choice == False:
    password_length = input("Please enter length of password (Minimum size is 8, max is 12): ") 
    for x in length_choice:
      if password_length == x:
        is_valid_choice = True

  print(password_randomiser(random_punctuation(2), random_numbers(2), random_letters(password_length - 4)))

main()