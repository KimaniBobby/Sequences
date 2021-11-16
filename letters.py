def main():

    letters = str.lower(input("Enter sentence:")) #dont space the sentence (the space will carry a value of 32 if added)

    numbers = []

    total = 0
    
    for letter in letters:
        
        number = ord(letter) - 96
        
        numbers.append(number)
   
        total = sum(numbers)

        print((numbers),end = " ")

        print(" ")

        print("The sum of the values is:",total)

        

main()