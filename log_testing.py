import sys
import datetime

ipAddresses = {}

def getDateFromText(line):
    firstBracket = line.index("[")
    secondBracket = line.index("]")
    dateString = line[(firstBracket + 1):secondBracket]
    time_format_IN = "%d/%b/%Y:%H:%M:%S %z"
    dateObj = datetime.datetime.strptime(dateString, time_format_IN)
    return dateObj

def addLogLineObject(logLine):
    # split based on quotes
    split_on_quotes = logLine.split('\"')
    # get the date from the first element f=of that split
    timeStamp = getDateFromText( split_on_quotes[0])
    # with that out of the way, we get ip address by taking
    # the first element of a split on spaces
    firstSplitArr = split_on_quotes[0].split(" ")
    ip_address = firstSplitArr[0]
    # from there, get the status code from a split of split_on_quotes[2]
    thirdSplitArr = split_on_quotes[2].split(" ")
    status_code = thirdSplitArr[1]
    # get user agent from split_on_quotes[5]
    user_agent = split_on_quotes[5]

    if ip_address not in ipAddresses:
        ipAddresses[ip_address] = {
            "count" : 1,
            "firstHit" : timeStamp,
            "lastHit" : timeStamp,
            "status_codes" : {
                status_code : 1
            },
            "user_agents" : {
                user_agent : 1
            }
        }
    else:
        ipAddresses[ip_address]["count"] += 1

        if timeStamp < ipAddresses[ip_address]["firstHit"]:
            ipAddresses[ip_address]["firstHit"] = timeStamp
        if timeStamp > ipAddresses[ip_address]["lastHit"]:
            ipAddresses[ip_address]["lastHit"] = timeStamp

        if status_code in ipAddresses[ip_address]["status_codes"]:
            ipAddresses[ip_address]["status_codes"][status_code] += 1
        else:
            ipAddresses[ip_address]["status_codes"][status_code] = 1

        if user_agent in ipAddresses[ip_address]["user_agents"]:
            ipAddresses[ip_address]["user_agents"][user_agent] += 1
        else:
            ipAddresses[ip_address]["user_agents"][user_agent] = 1
    
    return ipAddresses[ip_address]


# Get files to work with from command line arguments
fileList = sys.argv[1:]

# prep output file lines
outputLines = ["*****    Output from log_testing.py    *****\n", "*****             --  2022, Stephen Graham    *****\n"]

now = datetime.datetime.now()
outputLines.append("\nLast run on:  " + now.strftime("%b %d, %Y  %T:%M%p") + "\n")
outputLines.append("\nFiles:\n")
for file in fileList:
    outputLines.append(f"\t{file}\n")
outputLines.append("\n-----  Most Hits:  -----\n\n")

ipAddresses = {}

for fileName in fileList:
    theFile = open(fileName, 'r')
    lines = theFile.readlines()
    for i in range(10):
        myline = lines[i]
        addLogLineObject(myline)
    # # split based on quotes
    # split_on_quotes = myline.split('\"')
    # # get the date from the first element f=of that split
    # timeStamp = getDateFromText( split_on_quotes[0])
    # # with that out of the way, we get ip address by taking
    # # the first element of a split on spaces
    # firstSplitArr = split_on_quotes[0].split(" ")
    # ip_address = firstSplitArr[0]
    # # from there, get the status code from a split of [2]
    # thirdSplitArr = split_on_quotes[2].split(" ")
    # status_code = thirdSplitArr[1]

    # userAgent = split_on_quotes[5]

    # print(split_on_quotes)
    # time_format_OUT = "%A, %B %d, %Y - %I:%M %p"
    # print("Date: " + datetime.datetime.strftime(timeStamp, time_format_OUT))
    # print("ip address:  " + ip_address)
    # print("status code:  " + status_code)
    # print("user agent:  " + userAgent)
    print(ipAddresses)

# split_on_quotes[0] - ip address, client id, user id, [date], tls, ecdhe
# split_on_quotes[1] - client request
# split_on_quotes[2] - status code, size of return
# split_on_quotes[3] - referrer
# split_on_quotes[4] - user agent
# """
# Dictionary:
# { 222.222.222.222 : {
#     "count" : number,
#     "first_hit" : datetime object,
#     "lastst_hit" : datetime object,
#     "status_codes" : {'code1': count, 'code2' : count, ...},
#     "user_agents" : {'agent1' : count, 'agent2' : count, ...}
#     }
# }
# 09/May/2022:19:59:58 -0400
# Date format: "%d/%b/%Y:%H:%M:%S %z"
# out: "%b %b, %Y %H:%M:%S"
# """





    theFile.close()

