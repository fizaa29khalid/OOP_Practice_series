class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Reset current value for fresh iteration
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Using the Countdown class in a for-loop
cd = Countdown(5)

print("Countdown:")
for number in cd:
    print(number)
