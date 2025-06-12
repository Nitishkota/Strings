from collections import Counter

def is_anagram(str1, str2):
  
  str1 = str1.replace(" ", "").lower()
  str2 = str2.replace(" ", "").lower()

  if len(str1) != len(str2):
    return False

  count1 = Counter(str1)
  count2 = Counter(str2)

  return count1 == count2

string1 = "listen"
string2 = "silent"
print(f"'{string1}' and '{string2}' are anagrams: {is_anagram(string1, string2)}")

string3 = "hello"
string4 = "world"
print(f"'{string3}' and '{string4}' are anagrams: {is_anagram(string3, string4)}")

string5 = "The eyes"
string6 = "They see"
print(f"'{string5}' and '{string6}' are anagrams: {is_anagram(string5, string6)}")