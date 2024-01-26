#@author Elias Kotlyar
#@category Tuning
#@keybinding
#@menupath
#@toolbar

from ghidra.program.model.address import Address
from ghidra.program.model.address import AddressSet
from ghidra.program.model.block import IsolatedEntrySubModel
from ghidra.util import SystemUtilities


set = AddressSet()
listing = currentProgram.getListing()

initer = listing.getInstructions(currentProgram.getMemory(), True)
while initer.hasNext() and not monitor.isCancelled():
	instruct = initer.next()
	set.addRange(instruct.getMinAddress(), instruct.getMaxAddress())

iter = listing.getFunctions(True)
while iter.hasNext() and not monitor.isCancelled():
	f = iter.next()
	set.delete(f.getBody())

if set.getNumAddressRanges() == 0:
	popup("NO RESULTS - all instructions are contained inside functions")
	exit()

# go through address set and find the actual start of flow into the dead code
submodel = IsolatedEntrySubModel(currentProgram)
subIter = submodel.getCodeBlocksContaining(set, monitor)
codeStarts = AddressSet()
while subIter.hasNext():
	block = subIter.next()
	deadStart = block.getFirstStartAddress()
	codeStarts.add(deadStart)


for startAdr in codeStarts:
    phyAdr = startAdr.getMinAddress()
    print("Undef Func detected at: " + phyAdr.toString())
    createFunction(phyAdr, None)
