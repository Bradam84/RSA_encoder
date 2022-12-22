
def encoder():  # Opens and encrypts text file
    encode = open("encrypt.txt", "r")
    result = open("result.txt", "w")

    # Gets the public key from the users
    print("What is the first part of the public key?")
    public_key = int(input())
    print("What is the second part of the public key?")
    modulus = int(input())

    for line in encode:  # Reads each line of the text file to be encrypted
        coded_line = ""
        for letter in line:  # Reads each character of the line to be encrypted
            if letter == " ":  # Codes space characters to 32
                convert = 32
            elif letter == ",":  # Codes "," characters to 28
                convert = 28
            elif letter == ".":  # Codes "." characters to 27
                convert = 27
            elif letter == "'":  # Codes "'" characters to 29
                convert = 29
            else:
                convert = ord(letter) - 64  # Converts the Ascii character value and subtracts 64

            convert = (convert ** public_key) % modulus  # Applies RSA
            coded_line = coded_line + str(convert).zfill(2) + " "  # Stores the characters in string and adds space between numbers
        result.write(coded_line[0:-4] + " 32\n")  # Writes the encoded line to the result text also deletes the newline number and replaces it with 32
    encode.close()
    result.close()
    print("The file has been encrypted.\n")  # Prints a message letting the user know the file has been encrypted


def decoder():  # decodes an encrypted text file
    decode = open("decrypt.txt", "r")
    result = open("result.txt", "w")

    # Asks the user for the private key
    print("What is the first part of the private key?")
    private_key = int(input())
    print("What is the second part of the private key?")
    modulus = int(input())

    for line in decode:  # Reads each line of the text file to be decrypted
        decoded_line = ""
        for number in line.split():  # Reads each character of the line to be decrypted
            convert = (int(number) ** private_key) % modulus  # Applies the private key to the RSA
            if int(convert) == 32:  # Converts a few of the coded numbers to text characters
                convert = " "
            elif int(convert) == 27:
                convert = "."
            elif int(convert) == 28:
                convert = ","
            elif int(convert) == 29:
                convert = "-"
            elif int(convert) == 30:
                convert = "'"
            elif int(convert) == 31:
                convert = "\n"
            else:
                convert = chr(int(convert) + 64)  # Converts the numbers back to their Ascii value

            decoded_line = decoded_line + convert  # Stores the characters as they are decrypted
        result.write(decoded_line + "\n")  # Writes the line to the result text

    decode.close()
    result.close()
    print("The file has been decoded.\n")  # Informs the user that the process as been completed


if __name__ == '__main__':

    print("Are you encoding or decoding?")  # Asks the user if the user is going to encrypt or decrypt
    option = input()
    if option == "encode":
        encoder()
    elif option == "decode":
        decoder()
