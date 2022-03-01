""" Modulo principal do jogo
    """
from pokemon import PokemonAco, PokemonBicho
from pessoa import Player
from items import MochilaPequena, PokebolaPremium


eu = Player('Fernando')
mochila = MochilaPequena()
pokebola = PokebolaPremium()
pokemon = PokemonAco('Metal')
amigo_pokemon = PokemonBicho('Bicho')

print(mochila)
