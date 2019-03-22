
import os
import _winreg

def deleteKey(location, value):
	try:
		reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
		key = OpenKey(HKEY_LOCAL_MACHINE,location, 0, KEY_ALL_ACCESS)
		DeleteValue(key, value)
		CloseKey(key)
		return 1
	
	except:
		print("The registry value does not exist")
		return 0



def registryMain():	
	
	if os.name == 'nt':	# Checking if the operating System is Windows

		location = 'Software\Microsoft\Windows\CurrentVersion\Run'
		value = 'firefox.exe'
		ret = deleteKey(location, value)
		return ret
	
	else:
		print("Unsupported OS Version")
		return 0
