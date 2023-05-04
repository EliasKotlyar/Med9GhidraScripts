#TODO write a description for this script
#@author 
#@category Tuning
#@keybinding 
#@menupath 
#@toolbar 

# Creates a function:
def createFunction(cmdList):
	# Taken from: https://www.cs.uaf.edu/2011/fall/cs301/lecture/11_21_PowerPC.html
	preArr = ["stwu r1,-0x10(r1)", "mfspr r0,LR", "stw r0,0x14(r1)"]
	postArr = ["lwz r0,0x14(r1)","mtspr LR,r0","addi r1, r1, 0x10","blr"]
	return preArr + cmdList + postArr
	#return cmdList

def compileList(cmdList,address):
	currentAddress = address
	for cmd in cmdList:
		asm.assemble(toAddr(currentAddress),cmd)
		currentAddress = currentAddress +4

def relativeAddress(address):
	return	hex(address - 0x7ffff0)+"(r13)" 


asm = ghidra.app.plugin.assembler.Assemblers.getAssembler(currentProgram);
# Enable Boost Gauge:
ADDRESS_CWLDANZ = 0x1C6338
ADDRESS_CWLDANZ = ADDRESS_CWLDANZ + 0x400000
setByte(toAddr(ADDRESS_CWLDANZ),0x01)
createLabel(toAddr(ADDRESS_CWLDANZ), "CWLDANZ", True)
# Can Byte:
canByte5Addr = 0x8043c0
createLabel(toAddr(canByte5Addr), "mot7byte5", True)
# Absolute Pressure:
absolutePressure = 0x7fc99a
createLabel(toAddr(absolutePressure), "absolutePressure", True)

# Section where new Code will be saved:
sectionAddress1 = 0x47D000
# Original Call Code:



# Section 1:
section1CmdList = [
	# Loading Absolute Pressure in R4
	"lhz r12,"+relativeAddress(absolutePressure),
	# Load 0x8000 in R11:
	"lis r11, 0x0",
	"ori r11,r11, 0x8000",
	# Compare R11 with R4:
	"cmpw r11,r12",
	# If bigger, jump to location:
	"bgt 0x47D030",

	# IF smaller than 0x8000
	# Byteshift 8 times
	"srawi r12,r12,8",
	# Multiply with 100
	"li r11, 200",
	"mullw r12,r12,r11",
	"b 0x47D03C",


	# If bigger:
	# Byteshift 7 times
	"srawi r12,r12,7",
	# Multiply with 100
	"li r11, 100",
	"mullw r12,r12,r11",
	
	
	# Divide Result by 10
	"li r11, 10",
	"divw r12,r12,r11",
	# Divide by 20
	"li r11, 20",
	"divw r12,r12,r11",


	
	# Store R12 in CANByte5 Adress:
	"stb r12,"+relativeAddress(canByte5Addr),
	# Original Function Call:
	"li r3,0x8",
	"bl 0x004e8ff4",
]
compileList(createFunction(section1CmdList),sectionAddress1)




# Rewrite Section:
rewriteAddr = 0x503a98
asm.assemble(toAddr(rewriteAddr),"bl "+hex(sectionAddress1))

