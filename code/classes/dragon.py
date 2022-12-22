from pet import Pet
class Dragon(Pet):
    def __init__(self, name) -> None:
        super().__init__(name)

    def eat(self):
        print(f"{self.name}: CHOMP CHOMP")

    def play(self):
        print(f"{self.name}: RAWR XD")