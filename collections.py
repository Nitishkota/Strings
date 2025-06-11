from collections import Counter

def most_frequent_character(s):
  if not s:  # Handle empty string case
    return None

  char_counts = Counter(s)

  most_common_char = char_counts.most_common(1)[0][0]

  return most_common_char

text1 = "programming"
print(f"The most frequent character in '{text1}' is: {most_frequent_character(text1)}")

text2 = "google colab"
print(f"The most frequent character in '{text2}' is: {most_frequent_character(text2)}")

text3 = ""
print(f"The most frequent character in '{text3}' is: {most_frequent_character(text3)}")