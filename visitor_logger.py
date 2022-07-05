import os
from logged_visitor import LoggedVisitor
from datetime import datetime

class VisitorLogger:
    def __init__(self):
        self.ipAddressCounts = {}
        # will be an dictionary of the format:
        # { "199.199.19": 12, "146.45.12": 22 }
        self.loggedVisitors = {}
        # will be a dictionary of the format:
        # { "199.199.19": [LoggedVisitor object], "146.45.12": [LoggedVisitor object] }
        self.files = []
        # list of string filenames
    
    def getIpAddressCounts(self):
        return self.ipAddressCounts
    
    def getLoggedVisitors(self):
        return self.loggedVisitors

    def getFiles(self):
        return self.files

    def setFiles(self, *args):
        if len(args):
            for arg in args:
                self.files.append(str(arg))

    def countIpAddressVisits(self):
        if self.files:
            for fileName in self.files:
                theFile = open(fileName, 'r')

                for line in theFile:
                    firstSpace = line.index(" ")
                    addr = line[0:firstSpace]
                    if addr in self.ipAddressCounts:
                        self.ipAddressCounts[addr] += 1
                    else:
                        self.ipAddressCounts[addr] = 1

                theFile.close()

    def printIpAddressCounts(self):
        if self.ipAddressCounts:
            for address, count in self.ipAddressCounts.items():
                print(f"{address}:  {count}")
    
    def printTopXNumVisitors(self, x):
        """
            sort ipAddressCounts (returns an ordered list of tuples)
            loop and print x number of times (top x items)
        """
        sortedAddresses = sorted(self.ipAddressCounts.items(), key=lambda x:x[1], reverse=True)
        for i in range(x):
            print(f"{sortedAddresses[i][0]}:  {sortedAddresses[i][1]}")

    
    def breakDownLogLine(self, line):
        splitOnQuotes = line.split('"')
        firstSection = splitOnQuotes[0]
        firstSplitOnSpace = firstSection.split(' ')

        thisIpAddress = firstSplitOnSpace[0]
        if len(thisIpAddress) > 17:
            thisData = {}
        else:
            rawDate = firstSplitOnSpace[3][1:]
            dateFormat = "%d/%b/%Y:%H:%M:%S"
            thisTimeStamp = datetime.strptime(rawDate, dateFormat)

            thisSecurityProtocol = firstSplitOnSpace[5]

            thisCypherSuite = firstSplitOnSpace[6]
            print(splitOnQuotes)
            secondSplitOnSpace = splitOnQuotes[2].split(' ')
            thisStatusCode = secondSplitOnSpace[1]

            thisUserAgent = splitOnQuotes[5]

            thisData = {
                "address" : thisIpAddress,
                "timeStamp" : thisTimeStamp,
                "securityProtocol" : thisSecurityProtocol,
                "cypherSuite" : thisCypherSuite,
                "statusCode" : thisStatusCode,
                "agent" : thisUserAgent,
            }

        return thisData


    def createLoggedVisitors(self):
        if self.files:
            for fileName in self.files:
                theFile = open(fileName, 'r')
                lines = theFile.readlines()

                for line in lines:
                    lineData = self.breakDownLogLine(line)

                    if lineData:
                        if lineData["address"] not in self.loggedVisitors:
                            newVisitor = LoggedVisitor(lineData["address"], lineData["timeStamp"], lineData["securityProtocol"], lineData["cypherSuite"], lineData["statusCode"], lineData["agent"])
                            self.loggedVisitors[lineData["address"]] = newVisitor
                        else:
                            existingVisitor = self.loggedVisitors[lineData["address"]]
                            existingVisitor.incrementCount()
                            existingVisitor.processTimestamp(lineData["timeStamp"])
                            existingVisitor.addSecurityProtocol(lineData["securityProtocol"])
                            existingVisitor.addCypherSuite(lineData["cypherSuite"])
                            existingVisitor.addStatusCode(lineData["statusCode"])
                            existingVisitor.addUserAgent(lineData["agent"])

                            self.loggedVisitors[lineData["address"]] = existingVisitor

                theFile.close()

    def printLoggedVisitors(self):
        if self.loggedVisitors:
            print("*****    Logged Visitors:    *****")
            for addr, vData in self.loggedVisitors.items():
                spaces = " " * (15 - len(addr))
                print(f"{addr}:{spaces}count: {vData.getCount()} - first_hit: {vData.getFirstHit()} - Status Codes: {vData.getStatusCodes()}")

