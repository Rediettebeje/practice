# problem: 1
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

# instantiate of the class Pokemon 
my_pokemon = Pokemon("Pikachu", ["Electric"])

# print the name of the pokemon
print(my_pokemon.name)

# problem: 2
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(self.name + " I choose you! ")
        else:
            print(self.name +" is wild! Catch them if you can! ")

# instantiate of the class Pokemon
squirtle = Pokemon("Squirtle", ["Water"])

# call the print_pokemon method
squirtle.print_pokemon()

# problem: 3
# update squirtle Pokemon so that is_caught is updated to True

squirtle.is_caught = True
squirtle.print_pokemon()

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()

# problem: 5
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()