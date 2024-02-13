class FlagManager:
    def __init__(self):
        self.flags = {}

    def set_flag(self, flag_address, value):
        if flag_address not in self.flags:
            self.flags[flag_address] = 0
        self.flags[flag_address] = value

    def add_to_flag(self, flag_address, amount):
        if flag_address not in self.flags:
            self.flags[flag_address] = 0
        self.flags[flag_address] += amount

    def subtract_from_flag(self, flag_address, amount):
        if flag_address not in self.flags:
            self.flags[flag_address] = 0
        self.flags[flag_address] -= amount

    def set_bit_flag(self, flag_address, bit_position, value):
        if flag_address not in self.flags:
            self.flags[flag_address] = 0

        if value == 1:
            self.flags[flag_address] |= (1 << bit_position)
        else:
            self.flags[flag_address] &= ~(1 << bit_position)

manager = FlagManager()
