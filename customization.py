class Customize:
    def __init__(self, appname, appsource, appversion = "1.0", appicon = ""):
        self.appName = appname
        self.appSource = appsource
        self.appVersion = appversion
        self.appIcon = appicon
    def getName(self):
        return self.appName
    
    def getSource(self):
        return self.appSource
    
    def getVersion(self):
        return self.appVersion
    
    def getFullName(self):
        return self.getName() + " version " + self.getVersion()
    
    def getIcon(self):
        return self.appIcon