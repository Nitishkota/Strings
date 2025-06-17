import re

def is_palindrome(s):
  
  processed_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

  return processed_s == processed_s[::-1]

input_string = "A man, a plan, a canal: Panama"
print(is_palindrome(input_string))

input_string_2 = "race a car"
print(is_palindrome(input_string_2))