class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = self.happiness + 1
        print(f"{self.name} ate food. Hunger: {old_hunger} → {self.hunger}, Happiness increased to {self.happiness}.")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy: {old_energy} → {self.energy}.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = self.happiness + 2
            self.hunger = self.hunger + 1
            print(f"{self.name} played! Energy is now {self.energy}, happiness is {self.happiness}, hunger is {self.hunger}.")
        else:
            print(f"{self.name} is too tired to play. Let them rest first!")

    def get_status(self):
        print(f"📊 {self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print()

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        print(f"🎩 Tricks {self.name} knows: {', '.join(self.tricks) if self.tricks else 'None yet!'}")

