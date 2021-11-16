# asciicode.py
# a program that reads a sentence from the user and outputs a new string produced using a secret code


def main():

    print("This program converts a textual message into a sequence of numbers representing the Unicode encoding of the message.\n")
    
    # Get the message to encode

    message = input("Please enter the message: ")

    print("\n Here are the Unicode codes:")

    # Loop through the message and print out the Unicode values

    for encode in message:

        tobe = (ord(encode)+5)
        
        print (tobe, end ="")
   # print()  # blank line before prompt

main()

