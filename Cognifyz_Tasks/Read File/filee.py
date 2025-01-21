#______________________________________________


from collections import defaultdict

# Initialize a dictionary to count each letter
letter_count = defaultdict(int)

# Open and read the file
with open("name.txt", "r") as file:
    text = file.read()

# Count each letter in the text
for char in text:
    if char.isalpha():  # Check if the character is a letter
        letter_count[char] += 1

# Print the count of each letter
for letter, count in letter_count.items():
    print(f"The number of {letter} is {count}")
