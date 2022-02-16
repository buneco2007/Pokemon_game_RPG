"""Modulo de pokemons"""

import classes


class Pokemon(classes.Aco):
    """[Classe master pokemon]
    """

    def __init__(self, especie: str,
                 sangue: float = 100, lvl: int = 1, const: float = 1,
                 nome: str = None, ataque: float = 10, defesa: float = 2) -> None:
        self.especie = especie.capitalize()
        self.ataque = ataque
        self.defesa = defesa
        self.lvl = lvl
        self.const = const
        if nome:
            self.nome = nome
        else:
            self.nome = especie.capitalize()
        if sangue:
            self.sangue = sangue / 2 + lvl * (self.const + 1) - 1
            self.sangue_maximo = self.sangue
        else:
            self.sangue_maximo = self.sangue

    def __str__(self) -> str:
        return f'{self.nome}({self.lvl}) {self.sangue}/{self.sangue_maximo}'

    def atacar(self, pokemon):
        """[Funcao para atacar]

        Args:
            pokemon ([Pokemon]): [Informe o pokemon que deseja atacar]
        """
        print(f'{self.nome} atacou {pokemon.nome}')
        efetivi = self.efetividade(pokemon)
        pokemon.receber_dano(self.ataque, efetivi)
        if efetivi == 0:
            print(f'{pokemon.nome} e imune ao seu ataque!!!')
        elif efetivi == 0.5:
            print('Seu ataque nao e muito efetivo!!!')
        elif efetivi == 1:
            print('Seu ataque efetou normalmente!!')
        else:
            print('Seu ataque eh muito efetivo!!!')

    def receber_dano(self, dano: float, efetividade: float):
        """[Funcao para receber dano]

        Args:
            dano (float): [Informe o dano do inimigo]
        """
        calculo: float = (dano - self.defesa) * efetividade
        self.sangue = self.sangue - calculo
        print(f'{self.especie} recebeu {calculo} de dano!!!')

    def descansar(self):
        """Descansar e encher HP
        """
        valor_cura: float = (self.sangue / 10) * 1
        sangue_novo: float = self.sangue + valor_cura
        if sangue_novo > self.sangue_maximo:
            self.sangue = self.sangue_maximo
        else:
            self.sangue += valor_cura
        print(f'{self.especie} descansou e curou {valor_cura}!')

    def efetividade(self, pokemon) -> float:
        """Metodo para teste de efetividade de ataque

        Args:
            tipo (Str): Tipo de pokemon
        """
        if self.tipo in pokemon.forte:
            return 2
        if self.tipo in pokemon.normal:
            return 1
        if self.tipo in pokemon.fraco:
            return 0.5
        return 0


class PokemonAco(Pokemon):
    """Classe de pokemon de aco

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo aco
    """
    tipo = 'aco'.capitalize()


meu_pokemon = PokemonAco('Meu pokemon')
pokemon_amigo = PokemonAco('Pokemon do amigo')

meu_pokemon.atacar(pokemon_amigo)
