from collections import defaultdict

uppercase = [
    
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


file = open("name.txt", "r")
f = file.read()

letter_count = defaultdict(int)

for char in f:
    if char.isalpha():
        letter_count[char] += 1
        
for letter in sorted(letter_count.keys()):
    print(f"The number of {letter} is {letter_count[letter]}")