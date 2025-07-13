# Write a function that sorts a list of strings alphabetically.
# ["apple", "banana", "cherry", "kiwi", "grape"]

def sort_strings_alphabetically(strings_list):
    return sorted(strings_list)

fruits = ["apple", "banana", "cherry", "kiwi", "grape"]
sorted_fruits = sort_strings_alphabetically(fruits)

print(sorted_fruits)
