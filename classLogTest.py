from visitor_logger import VisitorLogger

log = VisitorLogger()

file1 = "exampleAccess.22020504"
#log.setFiles(file1)

file2 = "mnd_logs/access.443.20220505"
log.setFiles(file1, file2)

log.countIpAddressVisits()

log.getIpAddressCounts()
print("*" * 35)
log.printIpAddressCounts()
print("*" * 35)
log.printTopXNumVisitors(15)
print("*" * 35)
log.createLoggedVisitors()
log.printLoggedVisitors()