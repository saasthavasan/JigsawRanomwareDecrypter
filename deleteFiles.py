'''
this file is used to remove the dropped malicious files by Jigsaw Ransomware.
The two dropped malicious files and their directories will be removed from the system:
	drpbx.exe -------->	C:\User\<username>\Appdata\Roaming\Drpbx\drpbx.exe
	firefox.exe ------>	C:\User\<username>\Appdata\Roaming\Firefox\firefox.exe	
'''
import os

def deleteFile(paths):
	
	try:
		for path in paths:
			shutil.rmtree(path)
	except:
		return 0
	
	return 1
		



def DeleteMain():
	if os.version == 'nt':
		username = os.getlogin()
		paths = []
		paths.append(os.path.join('..','User',username,'Appdata','Roaming','Firefox'))
		paths.append(os.path.join('..','User',username,'Appdata','Roaming','Drpbx'))
		ret = deleteFile(paths)
	
		if ret == 1:
			return 1
		else
			print("Malicious Files not found")
			return 0 
	else:
		print("Unsupported OS version")
		return 0
