# Med9GhidraScripts
Ghidrascripts which will help disassembly of MED9.1 ECUs


## Usage

### med9-install.py
Setup Ghidra for MED9.1 Binary

1. Insert MED9.1 Binary(2MB) into Ghidra.
2. Select PowerPC 32 Bit (Default)
3. Run "med9-install.py" to install the memory-table and set the registers


### AddJsonMaps.py

Add Maps from a WINOLS Json File into Ghidra
1. Go to Winols, select your damos, select "Export to CSV/Json"
2. Tick all the boxes in the dialog(All Columns & Adresses as Hex)
3. Put the resulting JSON-File into the same folder as this script (Usually: C:\Users\<username>\Ghidrascripts
4. Rename the JSON-File to "golf5.json"
5. Run this Script.
6. All Maps will be marked as "bytes" and will be commented.

## Clearall.py

If the AddJsonMaps.py fails with the message that it cannot convert code into data-bytes on certain adresses(you ran the analysis before using AddJsonMaps!), you can use this script to unset the whole file. It will also remove the comments from AddJsonMaps.


