# **Jigsaw Ransomware Decrypter**

Jigsaw Ransomware Encrypts the system files and deletes them if we take too long to pay the ransom amount of $150 USD.

Full Analysis report of Jigsaw Ransomware can be found [here](https://github.com/saasthavasan/Malware-Analysis-Reports/tree/master/JigsawRansomware/Report).

## **Installing Dependencies**:

`pip install -r requirements.txt`

# **How to Use**:
This tool require Administrative privilages to function properly, use this tool in cmd opend as an admistrator.

`python jigsawDecrypter.py -<option>`


<Options>
For decrypting a paricular file:

`python jigsawDecrypter.py -i <inputfile Path>`

For decrypting entire directory:

`python jigsawDecrypter.py -i <inputfile Path>`

For Removing the dropped files and removing Registry Keys:

`python jigsawDecrypter.py -r`

## Examples

`python jigsawDecrypter.py -i Sample/Hello.txt.fun`

`python jigsawDecrypter.py -d Sample/`

`python jigsawDecrypter.py -r`


# **To Do**:

* **Searching for the default directory of encrypted files**
* **Porting the tool to python3 **
 list**

# **Disclaimer**:

As this software is **PROVIDED WITH ABSOLUTELY NO WARRANTY OF ANY KIND,YOU USE THIS TOOL AT YOUR OWN RISK!**
