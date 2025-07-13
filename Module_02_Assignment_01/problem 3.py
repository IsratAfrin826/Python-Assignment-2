# Write a Python program that creates a new list containing only the duplicate elements from the given list: [1, 5, 6, 5, 1, 2, 3].

def find_duplicates(input_list):
    duplicates = []
    seen = set()
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates


numbers = [1, 5, 6, 5, 1, 2, 3]
duplicate_numbers = find_duplicates(numbers)

print(duplicate_numbers)
