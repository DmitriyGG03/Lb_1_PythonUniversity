import sys
import msvcrt
import os


inputStrings = ""
data = []

while True:
    os.system('cls')
    print("Enter strings:")
    while True:
        inputStrings = input()
    
        if inputStrings == "exit":
            sys.exit()
        elif inputStrings == "":
            break
        else:
            data.append(inputStrings)

    if len(data) == 0:
        print("No data")
    
    print("Output result:")
    for str in data:
        print(str[0] + str[len(str) - 1])   
    print("\nPress any key to input again")
    msvcrt.getch()