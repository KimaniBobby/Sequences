#The program lists the powers of 2 in a table of some sorts

def power():

    for x in range(1,11):
        
        power_of_2 = 2 ** x
        
        power_of_1 = (1/x) ** 2
        
        print(x,"\t" "\t", power_of_2,"\t" "\t", "{0:0.3f}".format(power_of_1))

power()
