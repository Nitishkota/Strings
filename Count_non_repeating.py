from collections import Counter

def first_non_repeating_character(s):
  if not s:
    return -1  

  char_counts = Counter(s)

  for i in range(len(s)):
    if char_counts[s[i]] == 1:
      return i

  return -1 
text1 = "leetcode"
print(f"The index of the first non-repeating character in '{text1}' is: {first_non_repeating_character(text1)}")

text2 = "loveleetcode"
print(f"The index of the first non-repeating character in '{text2}' is: {first_non_repeating_character(text2)}")

text3 = "aabb"
print(f"The index of the first non-repeating character in '{text3}' is: {first_non_repeating_character(text3)}")

text4 = ""
print(f"The index of the first non-repeating character in '{text4}' is: {first_non_repeating_character(text4)}")
