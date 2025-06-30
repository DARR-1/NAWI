class User:
    def __init__(self, username, password, level, unlockedTopics=0):
        self.username = username
        self.password = password
        self.level = level
        self.unlockedTopics = unlockedTopics

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def setLevel(self, level):
        self.level = level

    def setUnlockedTopics(self, unlockedTopics):
        self.unlockedTopics = unlockedTopics

    def getUnlockedTopics(self):
        return self.unlockedTopics

    def getLevel(self, type=None):
        if type > 4:
            print("Invalid type")
            return None

        return self.level[type]
