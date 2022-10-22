#@author Elias Kotlyar
#@category Tuning
#@keybinding 
#@menupath 
#@toolbar 

startAddr = 0x400000
endAddr = 0x600000
clearListing(toAddr(startAddr),toAddr(endAddr))
for i in range(startAddr,endAddr):
	address = toAddr(i)
	if(getPreComment(address)):
		setPreComment(address,"")
	if(getPostComment(address)):
		setPostComment(toAddr(i),"")

