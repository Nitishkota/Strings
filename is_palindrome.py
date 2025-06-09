def is_palindrome(s):
  
  cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

  return cleaned_s == cleaned_s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome("hello"))
print(is_palindrome("madam"))