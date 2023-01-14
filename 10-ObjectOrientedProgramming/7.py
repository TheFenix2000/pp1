class Tv():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on =False

    def show_status(self):
        channel = ",channel "+str(self.channel_no) if self.is_on == True else ""
        status = "Tv is turned on" if self.is_on == True else "Tv is turned off"
        channel_name = self.channels[self.channel_no] if self.channel_no > 0 and self.channel_no < len(self.channels) else "Unknown channel"
        print(f"{status} {channel} ({channel_name})")

    def set_channel(self, new_channel):
        self.channel_no = new_channel

    def set_channels(self, channels_list):
        for channel in channels_list:
            self.channels.append(channel)
            
    def show_channels(self):
        show_list = self.channels if self.is_on == True else "Tv is turned off"
        print(show_list)


myTv = Tv()
myTv.show_status()
myTv.turn_on()
myTv.show_status()
myTv.set_channel(3)
myTv.show_status()
myTv.show_channels()
myTv.set_channels(['Polsat', "TVN", "TVP1", "TVP2"])
myTv.show_channels()
myTv.turn_off()
myTv.show_channels()
myTv.turn_on()
myTv.show_status()