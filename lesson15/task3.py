class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.position = 0

    def first_channel(self):
        self.position = 0
        return self.current_channel()

    def last_channel(self):
        self.position = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, channel_number):
        channel_number = channel_number - 1
        return self.channels[channel_number]

    def next_channel(self):
        self.position = (self.position + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.position = (self.position - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.position]

    def is_exist(self, name):
        return "Yes" if name in range(len(self.channels)) or name in self.channels else "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print('last', controller.last_channel())

for i in range(4):
    print('next', controller.next_channel())

print('first', controller.first_channel())

for i in range(5):
    print('previous', controller.previous_channel())

print('current', controller.current_channel())

print(controller.is_exist('BBC'))
print(controller.is_exist('BBS'))
