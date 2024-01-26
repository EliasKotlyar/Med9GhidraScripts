#TODO write a description for this script
#@author
#@category Tuning
#@keybinding
#@menupath
#@toolbar


from com.google.security.binexport import BinExportExporter
#TODO Add User Code Here
from java.io import File
fullpath = "test.BinExport"
from ghidra.app.util.exporter import BinaryExporter
bexp = BinExportExporter()
memory = currentProgram.getMemory()
monitor = getMonitor()
domainObj = currentProgram
f = File(fullpath)
bexp.export(f, domainObj, memory, monitor)