# def reveserse(s):
#     return s [::-1]

# # print(reveserse("Tejas"))


# def reverse_str(s):
#     reverse_string = " "

#     for char in s:
#         reverse_string = char + reverse_string
#     return reverse_string

# # print(reverse_str("Pawar"))

# print("python" [-3:])

def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

print(find_duplicates([1, 2, 3, 4, 2, 5, 1]))