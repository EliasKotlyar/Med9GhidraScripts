#TODO write a description for this script
#@author Elias Kotlyar
#@category Tuning
#@keybinding 
#@menupath 
#@toolbar 

memory = currentProgram.getMemory()
romblock = memory.getBlock(toAddr(0x0))
# Set Rom Block:
if(romblock):
	memory.moveBlock(romblock,toAddr(0x400000),monitor)
# Set Ram Block:
ramblock = memory.getBlock(toAddr(0x600000))
if(not ramblock):
	ramblock = memory.createUninitializedBlock("ram1", toAddr(0x600000), 0x200000, False)
ramblock.
# Set Registers:
context = currentProgram.getProgramContext()
r13 = context.getRegister("r13")
r2 = context.getRegister("r2")
start = toAddr(0x400000)
end = toAddr(0x600000)
r13Value = ghidra.util.NumericUtilities.unsignedLongToBigInteger(0x7ffff0)
r2Value = ghidra.util.NumericUtilities.unsignedLongToBigInteger(0x5c9ff0)
context.setValue(r13, start, end, r13Value);
context.setValue(r2, start, end, r2Value);

