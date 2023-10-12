class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            print("you're still alive!")
            print("%s has %d health and %d power." % (self.name, self.health, self.power))
        else:
            print("you're dead!")


class Hero(Character):
    def attack(self, other_person):
        print("%s says, 'I hate you!'" % self.name)
        print("%s attacked %s!" % (self.name, other_person.name))
        other_person.health -= self.power
        print("Goober how has", other_person.health, "health.")
    

class Goblin(Character):
    def taunt(self, other_person):      #in the assignment, this is another "attack" method
        print("%s says, 'YOUR MOTHER IS A MILF!'" % self.name)
        print("%s attacked %s!" % (self.name, other_person.name))
        other_person.health -= self.power
        print("Hermit how has", other_person.health, "health.")


Hermit = Hero("Hermit", 10, 5)
Goober = Goblin("Goober", 6, 2)


while Goober.alive() and Hermit.alive():
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")

    user_input = input("> ")

    if user_input == "1":
        # Hermit attacks Goober
        Goober.health -= Hermit.power
        print("You did %d damage to the Goofy Goober!" % Hermit.power)

        if Goober.health <= 0:
            print("The Goofy Goober is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goober is dead! Do you feel proud of yourself now?")

    if Goober.health > 0:
        # Goober attacks Hermit
        Hermit.health -= Goober.health
        print("Goober has done %d damage to you." % Goober.power)

        if Hermit.health <= 0:
            print("You're dead! WHOMP WHOMP!")

