#TODO write a description for this script
#@author
#@category Tuning
#@keybinding
#@menupath
#@toolbar


#TODO Add User Code Here
from java.io import File
fullpath = "test.bin"
from ghidra.app.util.exporter import BinaryExporter
bexp = BinaryExporter()
memory = currentProgram.getMemory()
monitor = getMonitor()
domainObj = currentProgram
f = File(fullpath)
bexp.export(f, domainObj, memory, monitor)