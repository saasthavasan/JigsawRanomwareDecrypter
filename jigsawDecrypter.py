import sys, getopt
import decryption
import registryRemover
import deleteFiles


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
		args = argv
	except :
		print('python jigsawDecrypter.py -<option>')
		print('For help command is:')
		print('python jigsawDecrypter.py -h')
		sys.exit(2)

	if args[0] == '-h':
		print('python jigsawDecrypter.py -<option>')
		print('\n<options>')
		print("\n1. For decrypting a paricular file:\npython jigsawDecrypter.py -i <inputfile> -o <outputfile>\n\n2. For deleting Registry Value and Dropped Files:\npython jigsawDecrypter.py -r")
		sys.exit()
	elif args[0] == '-i':
		try:
			inputFile = args[1]
			encryptedData = readFile(inputFile)
			decryptedData = decryption.Decrypt(encryptedData)
			writeFile(inputFile, decryptedData)
		except:
			print('jigsawRansomware.py -<option>')
			print('For help command is:')
			print('jigsawRansomware.py -h')
			sys.exit(2)
	
	elif args[0] == '-d'
		try:
                        inputFile = args[1]
                        encryptedData = readFile(inputFile)
                        decryptedData = decryption.Decrypt(encryptedData)
                        writeFile(inputFile, decryptedData)
                except:
                        print('jigsawRansomware.py -<option>')
                        print('For help command is:')
                        print('jigsawRansomware.py -h')
                        sys.exit(2)
	
	elif args[0] == '-r':
		ret1 = registryRemover.registryMain()
		if ret1 == 1:
			print("Registry Value Deleted Successfully")
		else:
			print("Cannot Delete Registry Value")
		ret2 = deleteFiles.deleteMain()
		if ret2 == 1:
			 print("Successfully deleted malicious Files")
		else:
			print("Malicious File Not Found")
	else:
		print('python jigsawDecrypter.py -<option>')
		print('For help command is:')
		print('python jigsawDecrypter.py -h')



if __name__ == "__main__":
	main(sys.argv[1:])
