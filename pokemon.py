"""Modulo de pokemons"""

import tipos
import classes


class Pokemon():
    """[Classe master pokemon]
    """

    def __init__(self, especie: str,
                 sangue: float = 100, lvl: int = 1, const: float = 1,
                 nome: str = None, ataque: float = 10, defesa: float = 2,
                 tipo: str = tipos.Tipos.aco, dificuldade: float = 100) -> None:
        self.especie = especie.capitalize()
        self.ataque = ataque
        self.defesa = defesa
        self.lvl = lvl
        if tipo:
            self.tipo = tipo
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
        if dificuldade:
            self.dificuldade = dificuldade

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
        print(efetivi)

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
        if self.tipo in pokemon.imune:
            return 0
        if self.tipo in pokemon.fraco:
            return 0.5
        return 1

    def ser_capturado(self, pokebola):
        """ser_capturado Classe que determina a probabilidade
        de ser capturado

        Arguments:
            pokebola -- Pokebola que sera usada
        """


class PokemonAco(Pokemon, classes.Aco):
    """Classe de pokemon aco

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo aco
        classes (str): Classe do pokemon
    """


class PokemonAgua(Pokemon, classes.Agua):
    """Classe de pokemon agua

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo agua
        classes (str): Classe do pokemon
    """


class PokemonBicho(Pokemon, classes.Bicho):
    """Classe de pokemon bicho

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo bicho
        classes (str): Classe do pokemon
    """


class PokemonDragao(Pokemon, classes.Dragao):
    """Classe de pokemon dragao

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo dragao
        classes (str): Classe do pokemon
    """


class PokemonEletrico(Pokemon, classes.Eletrico):
    """Classe de pokemon eletrico

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo eletrico
        classes (str): Classe do pokemon
    """


class PokemonFantasma(Pokemon, classes.Fantasma):
    """Classe de pokemon fantasma

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo fantasma
        classes (str): Classe do pokemon
    """


class PokemonFogo(Pokemon, classes.Fogo):
    """Classe de pokemon de fogo

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo fogo
        classes (str): Classe do pokemon
    """


class PokemonFada(Pokemon, classes.Fada):
    """Classe de pokemon fada

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo fada
        classes (str): Classe do pokemon
    """


class PokemonGelo(Pokemon, classes.Gelo):
    """Classe de pokemon gelo

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo gelo
        classes (str): Classe do pokemon
    """


class PokemonLuta(Pokemon, classes.Luta):
    """Classe de pokemon luta

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo luta
        classes (str): Classe do pokemon
    """


class PokemonNormal(Pokemon, classes.Normal):
    """Classe de pokemon normal

    Args:
        Pokemon (Pomemon): Instancia um pokemon do tipo normal
        classes (str): Classe do pokemon
    """


class PokemonPlanta(Pokemon, classes.Planta):
    """Classe de pokemon planta

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo planta
        classes (str): Classe do pokemon
    """


class PokemonPsiquico(Pokemon, classes.Psiquico):
    """Classe de pokemon Psiquico

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo Psiquico
        classes (str): Classe do pokemon
    """


class PokemonRocha(Pokemon, classes.Rocha):
    """Classe de pokemon Rocha

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo Rocha
        classes (str): Classe do pokemon
    """


class PokemonSinistro(Pokemon, classes.Sinistro):
    """Classe de pokemon Sinistro

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo Sinistro
        classes (str): Classe do pokemon
    """


class PokemonTerra(Pokemon, classes.Terra):
    """Classe de pokemon Terra

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo Terra
        classes (str): Classe do pokemon
    """


class PokemonVeneno(Pokemon, classes.Veneno):
    """Classe de pokemon Veneno

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo Veneno
        classes (str): Classe do pokemon
    """


class PokemonVoador(Pokemon, classes.Voador):
    """Classe de pokemon planta

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo Voador
        classes (str): Classe do pokemon
    """
