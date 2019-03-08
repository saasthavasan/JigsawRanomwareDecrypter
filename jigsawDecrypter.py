import sys, getopt
import decryption

def readFile(inputFile):

    inFile = open(inputFile, 'r')
    encryptedData = inFile.read()
    inFile.close()

    return encryptedData


def writeFile(inputFile, decryptedData):
    if inputFile[-4:] == ".fun":
        outFile = open(inputFile[:-4], 'w')
        outFile.write(decryptedData)
        outFile.close()
    else:
        outFile = open(inputFile, 'w')
        outFile.write(decryptedData)
        outFile.close()


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
    decryptedData = decryption.Decrypt(encryptedData)
    writeFile(inputFile, decryptedData)


if __name__ == "__main__":
    main(sys.argv[1:])
