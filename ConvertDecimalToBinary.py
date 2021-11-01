# Convert a decimal number into binary
# decimal will always be less than 1024

def convert_decimal():
    decimal = int(input("Enter a decimal number: "))
    quotient = int(decimal / 2)
    remainder0 = int(decimal % 2)
    pre_binary = []

    # Divide/mod every iteration until quotient = 0
    while quotient > 0:
        quotient //= 2
        remainder1 = quotient % 2
        pre_binary.append(remainder1)

    pre_binary.append(remainder0)

    # Convert the data into an integer
    conjoin1 = [str(i) for i in pre_binary]
    conjoin2 = "".join(conjoin1)
    binary = int(conjoin2)

    print("The decimal log10(" + str(decimal) + ") in binary is: log2(" + str(binary) + ")")


convert_decimal()
