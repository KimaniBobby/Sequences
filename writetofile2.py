#this code writes values to a text file (taskfive.txt)

def main():

    numbers = []

    for x in range (1,101):

        a = x ** 2

        b = x ** (1/2)

        z = open("taskfive.txt","w")

        c = (x,a,'{0:0.2f}'.format(b))

        numbers.append(c)

        z = open("taskfive.txt","w")

        z.write('\n'.join(numbers))

        z.close ()

        print(c)

print("The values have been written to the text file in the format (number,square of number and square root of number)")

main()


 #myfile.write('\n'.join(lines))