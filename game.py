""" Modulo principal do jogo
    """
from pokemon import PokemonAco
from pessoa import Player


eu = Player('Fernando')
mochila = eu.items[0]
pokemon = PokemonAco('Metal')

mochila.add_item('teste')
print(mochila)
