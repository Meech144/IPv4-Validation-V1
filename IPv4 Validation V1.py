#initial prompt for input

addr = input("please enter a valid IPv4 address in dot notation or enter quit to exit program: ")

#statement for input of "quit" to end program so if the value inside the container = to quit then end program

if addr == 'quit':
    print("Ending program")
    exit()
#if statement looking for and alphanumeric value inside the addr container, since IPv4 addresses cannot contain letters
#if either letters or numbers or a combination are found without dot notation, error output can be created

if addr.isalnum():
    print("Error invalid input")
    exit()

#splitting initial input into a list so each variable can now be checked, looking for the "." specifically to partition
#indexing is used to assign a new container to each part of the input to later be converted

z = addr.split(".")

num1 = z[0]
num2 = z[1]
num3 = z[2]
num4 = z[3]

#Now using the .isdigit function per container to see if each container has numbers inside as another error check
#The pass statement is used here because if it is a digit then we want to pass the check and if not print error

if num1.isdigit():
    pass

else:
    print("Error invalid input")
    exit()

if num2.isdigit():
    pass

else:
    print("Error invalid input")
    exit()

if num3.isdigit():
    pass

else:
    print("Error invalid input")
    exit()

if num4.isdigit():
    pass

else:
    print("Error invalid input")
    exit()

#in order to use comparisons like greater then,less than etc., we need to convert the containers to integers because
#the previous checks can only be used on strings as they are string functions

oct1 = int(num1)
oct2 = int(num2)
oct3 = int(num3)
oct4 = int(num4)

#we are now comparing the containers with each octet to a specific range to make sure we are getting an ip address in
#the network range and not the host or broadcast ranges.

if oct1 >=1 and oct1 <= 255:
    print("Octet one is validated")
else:
    print("Octet one is not validated")

if oct2 >=0 and oct2 <= 255:
    print("Octet two is validated")
else:
    print("Octet two is not validated")

if oct3 >=0 and oct3 <= 255:
    print("Octet three is validated")
else:
    print("Octet three is not validated")

if oct4 >=1 and oct4 <= 255:
    print("Octet four is validated")
else:
    print("Octet four is not validated")

#if all the numbers are now validated this is the last check to ensure that the IPv4 address has all the octets
#validated, and they are all in the network range

if oct1 >=1 and oct1 <= 255 and oct2 >=0 and oct2 <= 255 and oct3 >=0 and oct3 <= 255 and oct4 >=1 and oct4 <= 255:
    print("This is a valid IPv4 address")
else:
    print("This is not a valid IPv4 address")