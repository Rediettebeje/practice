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

# instantiate of the class Pokemon
squirtle = Pokemon("Squirtle", ["Water"])

# call the print_pokemon method
squirtle.print_pokemon()

# problem: 3
# update squirtle Pokemon so that is_caught is updated to True

squirtle.is_caught = True
squirtle.print_pokemon()