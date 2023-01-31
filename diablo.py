"""pass"""
import os
from random import randint, sample


class Personagem:
    """class Personagem"""

    def __init__(self, nome, vida, ataque, defesa) -> None:
        self.nome = nome
        self.vida_inicial = vida
        self.vida_atual = vida
        self.ataque = ataque
        self.defesa = defesa
        self.level: int = 1
        self.experiencia = 0

    def atacar(self, alvo: 'Monstro') -> None:
        """atacar(self, alvo)"""
        dano_real: int = self.ataque + randint(0, 10) - alvo.defesa
        dano_real: int = max(dano_real, 0)
        alvo.vida_atual -= dano_real
        print(f"{self.nome} atacou {alvo.nome} com dano {dano_real}.")

    def verifica_xp(self) -> bool:
        """verifica se vai subir de level"""
        return self.experiencia > 100

    def sobe_level(self) -> None:
        """sobre o level do Personagem e cura ele"""
        while self.verifica_xp():
            self.experiencia: int = self.experiencia - 100
            self.level += 1
            self.ataque += 4
            self.defesa += 1
            # cura o boneco e adiciona vida
            self.vida_atual: int = self.vida_inicial + 15
            # atualiza vida inicial para o novo valor de vida inicial
            self.vida_inicial: int = self.vida_atual

    def __str__(self) -> str:
        return (f'O {self.nome} (lvl {self.level} - xp {self.experiencia}) '
                f'está com hp={self.vida_atual} e tem atk={self.ataque} e '
                f'def={self.defesa}.')


class Guerreiro(Personagem):
    """class Guerreiro(Personagem)"""

    def __init__(self, nome, vida, ataque, defesa) -> None:
        Personagem.__init__(self, nome, vida, ataque, defesa)


class Monstro(Personagem):
    """class Monstro(Personagem)"""

    def __init__(self, nome, vida, ataque, defesa, recompensa) -> None:
        super().__init__(nome, vida, ataque, defesa)
        self.recompensa = recompensa

    def dar_xp(self, jog: Personagem) -> None:
        """dar_xp(self, jog)"""
        jog.experiencia += self.recompensa
        print(f"O {jog.nome} ganhou {self.recompensa} de xp.")

    @classmethod
    def cria_esqueleto(cls) -> 'Monstro':
        """cria_esqueleto(cls)"""
        return cls("Esqueleto", 50, 10, 2, 100)

    @classmethod
    def cria_goblin(cls) -> 'Monstro':
        """cria_goblin(cls)"""
        return cls("Goblin", 20, 8, 1, 20)

    @classmethod
    def cria_diablo(cls) -> 'Monstro':
        """cria_diablo(cls)"""
        return cls("Diablo", 250, 25, 8, 1000)

    @staticmethod
    def sorteia_monstro(qtd: int) -> list['Monstro']:
        """sorteia_monstro(qtd)"""
        monstros: list['Monstro'] = []
        for _ in range(qtd):
            num: int = randint(1, 10)

            if num < 6:
                monstros.append(Monstro.cria_goblin())
            elif num < 10:
                monstros.append(Monstro.cria_esqueleto())
            else:
                monstros.append(Monstro.cria_diablo())
        return monstros

    def __str__(self) -> str:
        return (f'O {self.nome} está com hp={self.vida_atual} e tem '
                f'atk={self.ataque} e def={self.defesa}.')


class Game:
    """classe para gerenciar a luta"""

    def __init__(self, jog: Personagem, qtd: int) -> None:
        self.jogador: Personagem = jog
        self.monstros: list[Monstro] = Monstro.sorteia_monstro(qtd)

    def iniciar_luta(self) -> None:
        """módulo responsável por realizar a luta até a morte do jogador ou até
        os monstros acabarem!"""
        monstro: Monstro = sample(self.monstros, 1)[0]

        print(f"{self.jogador.nome} entrou na arena para enfrentar {monstro.nome}.")

        # loop da batalha
        while True:
            # O jogador ataca o monstro
            jogador.atacar(monstro)
            # Verificando se o monstro está vivo
            if monstro.vida_atual <= 0:
                print(f"{monstro.nome} foi morto!")
                monstro.dar_xp(jogador)
                self.monstros.remove(monstro)
                self.jogador.sobe_level()
                # print(self.jogador)

                # fim de jogo
                if not self.monstros:
                    break

                monstro = sample(self.monstros, 1)[0]
                print(
                    f"\n---{self.jogador.nome} vai enfrentar {monstro.nome}.---")
            else:
                print(f"{monstro.nome} ainda está vivo.")

            monstro.atacar(jogador)
            # Verificando se o monstro está vivo
            if jogador.vida_atual <= 0:
                print(f"{jogador.nome} foi morto!")
                break
            print(f"{jogador.nome} ainda está vivo.")
            print()

        print(monstro)

    def __str__(self) -> str:
        return 'Board game'


os.system('cls')  # limpa a tela
print('*'*100)
jogador: Guerreiro = Guerreiro(nome="Boromir", vida=100, ataque=20, defesa=5)
jogo: Game = Game(jogador, 15)
print(jogo)
print(jogador)
jogo.iniciar_luta()
print(jogador)
