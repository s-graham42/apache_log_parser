import sys
import datetime

# Get files to work with from command line arguments
fileList = sys.argv[1:]

# prep output file lines
outputLines = ["*****    Output from ip_address_counter.py    *****\n", "*****             --  2022, Stephen Graham    *****\n"]

now = datetime.datetime.now()
outputLines.append("\nLast run on:  " + now.strftime("%b %d, %Y  %T:%M%p") + "\n")
outputLines.append("\nFiles:\n")
for file in fileList:
    outputLines.append(f"\t{file}\n")
outputLines.append("\n-----  Most Hits:  -----\n\n")

ipAddresses = {}

for fileName in fileList:
    theFile = open(fileName, 'r')

    for line in theFile:
        firstSpace = line.index(" ")
        addr = line[0:firstSpace]
        if addr in ipAddresses:
            ipAddresses[addr] += 1
        else:
            ipAddresses[addr] = 1

    theFile.close()

for address in sorted(ipAddresses, key=ipAddresses.get, reverse=True):
    if ipAddresses[address] > 500:
        formattedTotal = "{:,}".format(ipAddresses[address])
        numSpaces = 36 - (len(address)) - (len(formattedTotal))
        nextLine = address + (" " * numSpaces) + (formattedTotal) + "\n"
        outputLines.append(nextLine)

# print(outputLines)
output = open("detected_ip_addresses.txt", "w")
output.writelines(outputLines)
output.close()
