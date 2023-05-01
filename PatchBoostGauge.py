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


asm = ghidra.app.plugin.assembler.Assemblers.getAssembler(currentProgram);
# Enable Boost Gauge:

ADDRESS_CWLDANZ = 0x1C6338
ADDRESS_CWLDANZ = ADDRESS_CWLDANZ + 0x400000
setByte(toAddr(ADDRESS_CWLDANZ),0x01)
createLabel(toAddr(ADDRESS_CWLDANZ), "CWLDANZ", True)


# Section where new Code will be saved:
sectionAddress1 = 0x47D000
sectionAddress2 = 0x47D100
# Original Call Code:
canByte5Addr = 0x8043c0
relativeAddress = canByte5Addr - 0x7ffff0 

# Section 1:
section1CmdList = [
	# Load 0x1 into R12 Register
	"li r12,0x1",
	# Store R12 in CANByte5 Adress:
	"stb r12,"+hex(relativeAddress)+"(r13)",
	# Original Function Call:
	"li r3,0x8",
	"bl 0x004e8ff4",
]
compileList(createFunction(section1CmdList),sectionAddress1)

# Section 2:
section2CmdList = [
	# Load 0x2 into R12 Register
	"li r12,0x2",
	# Store R12 in CANByte5 Adress:
	"stb r12,"+hex(relativeAddress)+"(r13)",
	# Original Function Call:
	"li r3,0x8",
	"bl 0x004e8ff4",
]
compileList(createFunction(section2CmdList),sectionAddress2)




# Rewrite Section:
rewriteAddr = 0x503a98
asm.assemble(toAddr(rewriteAddr),"bl "+hex(sectionAddress1))

rewriteAddr = 0x573590
asm.assemble(toAddr(rewriteAddr),"bl "+hex(sectionAddress2))
