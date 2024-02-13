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

    def print_flags(self):
        print("Current Flags:")
        for flag_address, value in self.flags.items():
            print(f"Flag {flag_address}: {value}")


# Example usage:
manager = FlagManager()

# Set flag 'a6' to 1
manager.set_flag('a6', 1)

# Add 3 to flag '1d'
manager.add_to_flag('1d', 3)

# Subtract 2 from flag '18'
manager.subtract_from_flag('18', 2)

# Add 1 to flag 'af'
manager.add_to_flag('af', 1)

# Set bit 2 of flag '04' to 1
manager.set_bit_flag('04', 2, 1)

# Print current flags
manager.print_flags()
