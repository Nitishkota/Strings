def remove_duplicates_in_string(s):
  seen = set()
  result = []
  for char in s:
    if char not in seen:
      seen.add(char)
      result.append(char)
  return "".join(result)

text = "good times"
print(remove_duplicates_in_string(text))