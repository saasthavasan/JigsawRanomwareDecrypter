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
