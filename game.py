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

eu.pegar_item(mochila)
eu.add_item_mochila(pokebola, mochila)
eu.mostrar_items()
