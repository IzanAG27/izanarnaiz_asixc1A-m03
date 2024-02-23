class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def get_hit(self, attack):
        self.health -= attack
        print(f"{self.name} was hit and lost {attack} health points. Remaining health: {self.health}")

    def do_attack(self, other):
        if self.is_alive():
            print(f"{self.name} attacks {other.name}!")
            other.get_hit(self.attack)
        else:
            print(f"{self.name} is unable to attack because they are out of health.")


def play_game():
    char1 = Character("Charmander", 30, 5)
    char2 = Character("Squirtle", 35, 4)

    while char1.is_alive() and char2.is_alive():
        char1.do_attack(char2)
        if char2.is_alive():
            char2.do_attack(char1)

    if char1.is_alive():
        print(f"{char1.name} wins!")
    else:
        print(f"{char2.name} wins!")

play_game()