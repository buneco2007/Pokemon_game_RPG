""" Modulo para apresentacao de erros
    """
from typing import Type
from pokemon import Pokemon


class Erro(object):
    """Erro Classe que define os erros do jogo

    Arguments:
        object -- Object
    """
    @staticmethod
    def error_001(pokemon: Type[Pokemon]):
        """error_001 Erro de captura de pokemon

        Arguments:
            pokemon -- Pokemon que falhou em capturar
        """
        print(f'Falha ao capturar o pokemon {pokemon}')


class Sucesso(object):
    """Sucesso Classe que define as mensagens de sucesso

    Arguments:
        object -- Object
    """
    @staticmethod
    def sucesso_001(nome: str, pokemon: Type[Pokemon]):
        """sucesso_001 Capturado com sucesso.
        """
        print(f'{nome} capturou {pokemon}')
