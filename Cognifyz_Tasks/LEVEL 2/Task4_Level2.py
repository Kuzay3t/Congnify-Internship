sequence = []
number = int(input("Enter a number: "))

def sequence_generator(n):
    sequence.append(0)
    sequence.append(1)
    for i in range(1, n):
        sequence.append(sequence[i] + sequence[i-1])
    print(sequence)
        
sequence_generator(number)