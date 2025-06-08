def reverse_string_loop(s):
  reversed_s = ""
  for char in s:
    reversed_s = char + reversed_s
  return reversed_s

string1 = "hello"
reversed_string1 = reverse_string_loop(string1)
print(reversed_string1)

string2 = "Python"
reversed_string2 = reverse_string_loop(string2)
print(reversed_string2)