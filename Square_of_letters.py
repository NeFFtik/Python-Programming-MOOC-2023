alphabet = ["none", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet_dictionary = {}

for key in range(len(alphabet)):
    alphabet_dictionary[key] = alphabet[key]

layers = int(input("Layers:"))
grid = (layers * 2) - 1

block_of_letters = {}
for lines in range(grid):
    block_of_letters[lines] = [] 

for letters in range(grid):
    block_of_letters[letters] += grid * alphabet_dictionary[layers]

left_border = 1
right_border = grid - 1
letter_down = -1

def hash():
        for line in range(left_border, right_border):
            
                for letter in range(left_border, right_border):
                    block_of_letters[line][letter] = alphabet_dictionary[layers + letter_down]

for test in range(layers - 1):
        hash()
        left_border +=  1
        right_border -= 1
        letter_down +=  -1    
            
        
for i in range(len(block_of_letters)):
    print("".join(block_of_letters[i]))