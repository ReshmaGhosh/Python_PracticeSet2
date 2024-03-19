# Find the first non-repeating character

input_str = "teeteraabcdd"

for char in input_str:
    print(char)
    if input_str.count(char)==1:
        print("Char is: ",char)
        break