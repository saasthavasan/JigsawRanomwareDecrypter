import Decrypt.py
import os
import decyption.py




def directoryDecrypt(path):
	if os.version == 'nt':
		dirListing = os.listdir(path)
		fileList = []
		counter = 0
		for item in dirListing:
			if ".fun" in item:
			fileList.append(path+'\\'+item)
		for item in fileList:
			ret = decryption.decryptFile(item)
			if ret == 1:
				print("Decrypted " + item)
				counter = counter + 1
			else:
				print("Unable to decrypt" + item)
		if counter == len(fileList):
			return 1
		else:
			return 0
	else:
		print("Unsupported OS Version")
		return 0
