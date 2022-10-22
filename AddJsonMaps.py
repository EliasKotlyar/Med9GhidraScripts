#@author Elias Kotlyar
#@category Tuning
#@keybinding 
#@menupath 
#@toolbar 

import os
import json
pathname = os.path.dirname(__file__)
f = open(pathname+"/golf5.json", "r")
content = f.read()
print(content)
content = content.encode('utf-8')
contentJson = json.loads(content)
for map in contentJson["maps"]:
	startAddr = map["Fieldvalues.StartAddr"]
	startAddr = startAddr.replace("$","")
	startAddr = int(startAddr, 16)
	startAddr = startAddr + 0x400000
	rows = int(map["Rows"])
	columns = int(map["Columns"])
	size =  rows * columns
	if map["DataOrg"] == "eHiLo":
		size = size * 2
		size = size - 2
		pass
	else:
		size = size - 1;
	name = map["IdName"]
	endAddr = startAddr + size
	print(hex(startAddr),hex(endAddr),size,name)
	setPreComment(toAddr(startAddr),name + " START")
	setPostComment(toAddr(endAddr),name + " END")
	for i in range(startAddr,endAddr):
		createByte(toAddr(i))
		pass
