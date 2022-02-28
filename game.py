""" Modulo principal do jogo
    """
from pokemon import PokemonAco, PokemonBicho
from pessoa import Player
from items import MochilaGrande, PokebolaPremium


eu = Player('Fernando')
mochila = MochilaGrande()
pokebola = PokebolaPremium()
pokemon = PokemonAco('Metal')
amigo_pokemon = PokemonBicho('Bicho')

print(mochila)
