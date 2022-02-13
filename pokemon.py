"""Modulo de pokemons"""


class Pokemon():
    """[Classe master pokemon]
    """

    def __init__(self, tipo: str, especie: str,
                 ataque: float, defesa: float,
                 sangue: float = 100, lvl: int = 1, const: float = 8) -> None:
        """[summary]

        Args:
            tipo (str): [Tipo]
            especie (str): [Especie]
            ataque (float): [Valor do ataque]
            defesa (float): [Valor da defesa]
            sangue (float, optional): [Quantidade de HP]. Defaults to 100.
            lvl (int, optional): [Lvl do pokemon]. Defaults to 1.
        """
        self.tipo = tipo.capitalize()
        self.especie = especie.capitalize()
        self.ataque = ataque
        self.defesa = defesa
        self.const = const
        if sangue:
            self.sangue = sangue / 2 + lvl * (self.const + 1) - 1
            self.sangue_maximo = self.sangue
        self.lvl = lvl

    def __str__(self) -> str:
        """[Funcao str padrao]

        Returns:
            [str]: [Retorna a descricao do pokemon]
        """
        return f'lvl: {self.lvl} {self.especie} ({self.tipo}) HP: {self.sangue}'

    def atacar(self, pokemon):
        """[Funcao de ataque]

        Args:
            pokemon ([Pokemon]): [Especifica um pokemon]
        """
        print(f'{self.especie} atacou {pokemon.especie}')
        pokemon.receber_dano(self.ataque)

    def receber_dano(self, dano: float):
        """[Funcao de receber dano]

        Args:
            dano (float): [Recebe o ataque do inimigo]
        """
        calculo = dano - self.defesa
        self.sangue = self.sangue - calculo
        print(f'{self.especie} recebeu {calculo} de dano!!!')

    def descansar(self):
        """[Funcao de descanso, regenera o HP]
        """
        valor_cura: float = (self.sangue / 10) * 1
        sangue_novo: float = self.sangue + valor_cura
        if sangue_novo > self.sangue_maximo:
            self.sangue = self.sangue_maximo
        else:
            self.sangue += valor_cura
        print(f'{self.especie} descansou e curou {valor_cura}!')


meupokemon = Pokemon('fogo', 'charmander', 20, 10, 100, 100, 8)
inimigopokemon = Pokemon('fogo', 'charmander', 20, 10, 100, 1, 8)

print(meupokemon)
print(inimigopokemon)
