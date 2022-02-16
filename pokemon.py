"""Modulo de pokemons"""

import tipos


class Pokemon():
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
        print(f'{self.especie} atacou {pokemon.especie}')
        pokemon.receber_dano(self.ataque)

    def receber_dano(self, dano: float, efetividade: float):
        """[Funcao para receber dano]

        Args:
            dano (float): [Informe o dano do inimigo]
        """
        calculo: float = (dano * efetividade) - self.defesa
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


class PokemonAco(Pokemon):
    """Classe de pokemon de aco

    Args:
        Pokemon (Pokemon): Instancia um pokemon do tipo aco
    """
    tipo: str = tipos.Tipos.aco
    normal: list[str] = [tipos.Tipos.bicho, tipos.Tipos.dragao, tipos.Tipos.fantasma,
                         tipos.Tipos.luta, tipos.Tipos.normal, tipos.Tipos.planta,
                         tipos.Tipos.psiquico, tipos.Tipos.sinistro, tipos.Tipos.terra,
                         tipos.Tipos.veneno, tipos.Tipos.voador]
    fraco: list[str] = [tipos.Tipos.aco, tipos.Tipos.agua, tipos.Tipos.eletrico,
                        tipos.Tipos.fogo]
    forte: list[str] = [tipos.Tipos.fada, tipos.Tipos.gelo, tipos.Tipos.rocha]
    imune: list[str] = []

    def efetividade(self, pokemon) -> float:
        """Metodo para teste de efetividade de ataque

        Args:
            tipo (Str): Tipo de pokemon
        """
        if self.tipo in pokemon.forte:
            return 2
        elif self.tipo in pokemon.normal:
            return 1
        elif self.tipo in pokemon.fraco:
            return 0.5
        else:
            return 0


class PokemonAgua(Pokemon):
    """Classe de pokemon de agua

    Args:
        Pokemon (Pokemon): Instancia um pokemon de agua
    """
    tipo = tipos.Tipos.agua


class PokemonBicho(Pokemon):
    """Classe de pokemon de bicho

    Args:
        Pokemon (Pokemon): Instancia um pokemon de bicho
    """
    tipo = tipos.Tipos.bicho


class PokemonDragao(Pokemon):
    """Classe de pokemon de dragao

    Args:
        Pokemon (Pokemon): Instancia um pokemon de dragao
    """
    tipo = tipos.Tipos.dragao


class PokemonEletrico(Pokemon):
    """Classe de pokemon eletrico

    Args:
        Pokemon (Pokemon): Instanciar um pokemon do tipo eletrico
    """
    tipo = tipos.Tipos.eletrico


class PokemonFantasma(Pokemon):
    """Classe de pokemon fantasma

    Args:
        Pokemon (Pokemon): Instanciar um pokemon do tipo fantasma
    """
    tipo = tipos.Tipos.fantasma


class PokemonFogo(Pokemon):
    """Classe de pokemon fogo

    Args:
        Pokemon (Pokemon): Instanciar um pokemon do tipo fogo
    """
    tipo = tipos.Tipos.fogo


class PokemonFada(Pokemon):
    """Classe de pokemon fada

    Args:
        Pokemon (Pokemon): Instanciar um pokemon do tipo fada
    """
    tipo = tipos.Tipos.fada


class PokemonGelo(Pokemon):
    """Classe de pokemon de gelo

    Args:
        Pokemon (Pokemon): Instancia um pokemon de gelo
    """
    tipo = tipos.Tipos.gelo


class PokemonLuta(Pokemon):
    """Classe de pokemon de luta

    Args:
        Pokemon (Pokemon): Instancia um pokemon de luta
    """
    tipo = tipos.Tipos.luta


class PokemonNormal(Pokemon):
    """Classe de pokemon de normal

    Args:
        Pokemon (Pokemon): Instancia um pokemon normal
    """
    tipo = tipos.Tipos.normal


class PokemonPlanta(Pokemon):
    """Classe de pokemon de planta

    Args:
        Pokemon (Pokemon): Instancia um pokemon planta
    """
    tipo = tipos.Tipos.planta


class PokemonPsiquico(Pokemon):
    """Classe de pokemon de psiquico

    Args:
        Pokemon (Pokemon): Instancia um pokemon psiquico
    """
    tipo = tipos.Tipos.psiquico


class PokemonRocha(Pokemon):
    """Classe de pokemon de rocha

    Args:
        Pokemon (Pokemon): Instancia um pokemon rocha
    """
    tipo = tipos.Tipos.rocha


class PokemonSinistro(Pokemon):
    """Classe de pokemon sinistro

    Args:
        Pokemon (Pokemon): Instanciar um pokemon sinistro
    """
    tipo = tipos.Tipos.sinistro


class PokemonTerra(Pokemon):
    """Classe de pokemon de terra

    Args:
        Pokemon (Pokemon): Instancia um pokemon de terra
    """
    tipo = tipos.Tipos.terra


class PokemonVeneno(Pokemon):
    """Classe de pokemon de veneno

    Args:
        Pokemon (Pokemon): Instancia um pokemon de veneno
    """
    tipo = tipos.Tipos.veneno


class PokemonVoador(Pokemon):
    """Classe de pokemon de voador

    Args:
        Pokemon (Pokemon): Instancia um pokemon voador
    """
    tipo = tipos.Tipos.voador


meu_pokemon = PokemonAco('Metal')

print(meu_pokemon.tipo)
