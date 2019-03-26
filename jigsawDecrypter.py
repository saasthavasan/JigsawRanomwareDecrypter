import sys, getopt
import decryption
import registryRemover


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
		print('jigsawRansomware.py -<option>')
		print('For help command is:')
		print('jigsawRansomware.py -h')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('python jigsawRansomware.py -<option>')
			print('\n<options>')
			print("\n1. For decrypting a paricular file:\npython jigsawRansomware.py -i <inputfile> -o <outputfile>\n\n2. For deleting Registry Value:\npython jigsawRansomware.py -a")
	
			sys.exit()
		elif opt == '-i':
			inputFile = arg
			encryptedData = readFile(inputFile)
        		decryptedData = decryption.Decrypt(encryptedData)
        		writeFile(inputFile, decryptedData)

		elif opt == '-r':
			ret = registryRemover.registryMain()
			if ret == 1:
				print("Registry Value Deleted Successfully")
			else:
				print("Cannot Delete Registry Value")

if __name__ == "__main__":
	main(sys.argv[1:])
