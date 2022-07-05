class LoggedVisitor:
    def __init__(self, address, timeStamp, securityProtocol, cypherSuite, statusCode, agent):
        self.address = address
        self.count = 1
        self.first_hit = timeStamp
        self.last_hit = timeStamp
        self.security_protocols = [securityProtocol]
        self.cypher_suites = [cypherSuite]
        self.status_codes = [statusCode]
        self.user_agents = [agent]
    
    def __str__(self):
        return (f'{self.address} - count: {self.count} - first_hit: {self.first_hit} - status codes: {self.status_codes}')

    def getAddress(self):
        return self.address
    
    def getCount(self):
        return self.count

    def getFirstHit(self):
        return self.first_hit

    def getLastHit(self):
        return self.last_hit

    def getSecurityProtocols(self):
        return self.security_protocols

    def getCypherSuites(self):
        return self.cypher_suites

    def getStatusCodes(self):
        return self.status_codes

    def getUserAgents(self):
        return self.user_agents

    def incrementCount(self):
        self.count += 1

    def processTimestamp(self, datetimeObj):
        if datetimeObj < self.first_hit:
            self.first_hit = datetimeObj

        if datetimeObj > self.last_hit:
            self.last_hit = datetimeObj
    
    def addSecurityProtocol(self, securityProtocol):
        if securityProtocol not in self.security_protocols:
            self.security_protocols.append(securityProtocol)
    
    def addCypherSuite(self, cypherSuite):
        if cypherSuite not in self.cypher_suites:
            self.cypher_suites.append(cypherSuite)

    def addStatusCode(self, statusCode):
        if statusCode not in self.status_codes:
            self.status_codes.append(statusCode)

    def addUserAgent(self, userAgent):
        if userAgent not in self.user_agents:
            self.user_agents.append(userAgent)