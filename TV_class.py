class TV:
    def __init__(self,volumeLevel = 1):
        self.channel = 1
        self.volumeLevel = volumeLevel
        self.on = False

    def turnOn(self):
        self.on = True
    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self,channel):
        if self.on and 1<=self.channel <=120:
            self.channel = channel

    def getvolumeLevel(self):
        return self.volumeLevel

    def setVolume(self,volumeLevel):
        if self.on and  1<= self.volumeLevel <= 10:
            self.volumeLevel = volumeLevel

    def channelUP(self):
        if self.on and 1 <self.channel <120:
            self.channel += 1
    def channelDOWN(self):
        if self.on and 1 <self.channel <120:
            self.channel -= 1

    def volumeUP(self):
        if self.on and 1<= self.volumeLevel<=10:
            self.volumeLevel +=1
    def volumeDOWN(self):
        if self.on and 1 <= self.volumeLevel <= 10:
            self.volumeLevel -= 1

