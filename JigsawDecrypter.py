import sys, getopt
from Crypto.Cipher import AES

def Decrypt(encryptedData):

# Extracted key from Jigsaw Ransomware
    key = ':\x82,\x03\x0c\x05\xdbw\x08\t\n\x0b\x0c\r\x0e\r'
# Extracted Initialization Vector(iv) from the Jigsaw
    iv = '\x00\x01\x00\x03\x05\x03\x00\x01\x00\x00\x02\x00\x06\x07\x06\x00'

# Creating AES object
    obj = AES.new(key, AES.MODE_CBC, iv)
    decryptedData = obj.decrypt(encryptedData)

    return decryptedData

def readFile(inputFile):
    encryptedData = ""

    with open(inputFile, 'r') as file1:
        encryptedData = file1.read()
        file1.close()
    return encryptedData


def writeFile(inputFile, decryptedData):
    if inputFile[-4:] == ".fun":
        with open(inputFile[:-4], 'w') as file2:
            file2.write(decryptedData)
            file2.close()
    else:
        with open(inputFile, 'w') as file2:
            file2.write(decryptedData)
            file2.close()


def main(argv):
    try:
        # Cheking for correct arguments
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('jigsawRansomware.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('jigsawRansomware.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg

    encryptedData = readFile(inputFile)
    decryptedData = Decrypt(encryptedData)
    writeFile(inputFile, decryptedData)


if __name__ == "__main__":
    main(sys.argv[1:])
