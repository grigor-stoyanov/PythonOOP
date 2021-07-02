from pokemon import Pokemon


class Trainer:
    def __init__(self, name, pokemons=None):
        self.name = name
        if pokemons is None:
            pokemons = []
        self.pokemons = pokemons

    def add_pokemon(self, pokemon: object):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return f'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        for obj in self.pokemons:
            if obj.name == pokemon_name:
                self.pokemons.remove(obj)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n" \
               f"{chr(10).join(['- ' + obj.pokemon_details() for obj in self.pokemons])}"


if __name__ == '__main__':
    trainer2 = Trainer("Ash", [Pokemon("Pikachu", 90)])
    pokemon = Pokemon("Pikachu", 90)
    print(pokemon.pokemon_details())
    trainer = Trainer("Ash")
    print(trainer.add_pokemon(pokemon))
    second_pokemon = Pokemon("Charizard", 110)
    print(trainer.add_pokemon(second_pokemon))
    print(trainer.add_pokemon(second_pokemon))
    print(trainer.release_pokemon("Pikachu"))
    print(trainer.release_pokemon("Pikachu"))
    print(trainer.add_pokemon(pokemon))
    print(trainer.trainer_data())
