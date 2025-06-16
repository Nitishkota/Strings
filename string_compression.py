def string_compression(s):
  
  if not s:
    return ""

  compressed = []
  count = 1

  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      count += 1
    else:
      compressed.append(s[i-1])
      compressed.append(str(count))
      count = 1

  
  compressed.append(s[-1])
  compressed.append(str(count))

  return "".join(compressed)

input_string = "aaabbccc"
compressed_string = string_compression(input_string)
print(compressed_string)

input_string_2 = "aabbcde"
compressed_string_2 = string_compression(input_string_2)
print(compressed_string_2)