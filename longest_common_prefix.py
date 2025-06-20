def longest_common_prefix(strs):
   
    if not strs:
        return ""

    strs.sort()

    first_str = strs[0]
    last_str = strs[-1]

    prefix = ""
    for i in range(min(len(first_str), len(last_str))):
        if first_str[i] == last_str[i]:
            prefix += first_str[i]
        else:
            break

    return prefix

input_strings = ["flower", "flow", "flight"]
common_prefix = longest_common_prefix(input_strings)
print(common_prefix)

input_strings_2 = ["dog", "racecar", "car"]
common_prefix_2 = longest_common_prefix(input_strings_2)
print(common_prefix_2)

input_strings_3 = ["", "b"]
common_prefix_3 = longest_common_prefix(input_strings_3)
print(common_prefix_3)