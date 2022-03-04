""" Modulo para apresentacao de erros
    """


from pokemon import Pokemon


class Erro(object):
    """Erro Classe que define os erros do jogo

    Arguments:
        object -- Object
    """
    @staticmethod
    def error_001(pokemon: Pokemon):
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
    def sucesso_001(nome: str, pokemon: Pokemon):
        """sucesso_001 Capturado com sucesso.
        """
        print(f'{nome} capturou {pokemon}')


class Geral(object):
    """Message Classe que define as mensagens gerais

    Arguments:
        object -- Object
    """
    @staticmethod
    def geral_001(nome: str):
        """geral_001 Itens em posse

        Arguments:
            nome -- Nome da pessoa
        """
        print(f'Items em posse de {nome}')
