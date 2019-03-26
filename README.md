# **Jigsaw Ransomware Decrypter**

Jigsaw Ransomware Encrypts the system files and deletes them if we take too long to pay the ransom amount of $150 USD.

Full Analysis report of Jigsaw Ransomware can be found [here](https://github.com/saasthavasan/Malware-Analysis-Reports/tree/master/JigsawRansomware/Report).

## **Installing Dependencies**:

`sudo pip install -r requirements.txt`

# **How to Use**:

`python jigsawRansomware.py -<option>`


<Options>
For decrypting a paricular file:

`python jigsaw -i <inputfile Path>``

For Removing the dropped files and removing Registry Keys:

`python jigsaw -r`

## Examples

`python jigsawDecrypter.py -i Sample/Hello.txt.fun`

`python jigsawDecrypter.py -r`


# **To Do**:

* **Adding support for scanning directories**
* **Searching for the default directory of encrypted files list**

# **Disclaimer**:

As this software is **PROVIDED WITH ABSOLUTELY NO WARRANTY OF ANY KIND,YOU USE THIS TOOL AT YOUR OWN RISK!**
