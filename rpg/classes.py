"""pass"""
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
        """ataca o monstro causando x de dano"""
        dano_real: int = self.ataque + randint(0, 10) - alvo.defesa
        dano_real: int = max(dano_real, 0)
        alvo.vida_atual -= dano_real
        print(f"{self.nome} atacou {alvo.nome} com dano {dano_real}.")

    def sobe_level(self) -> None:
        """sobre o level do Personagem, cura ele e atualiza o valor base da
        vida do personagem"""
        while self.experiencia > 100:
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
    """classe guerreira do jogador"""

    def __init__(self, nome, vida, ataque, defesa) -> None:
        Personagem.__init__(self, nome, vida, ataque, defesa)


class Monstro(Personagem):
    """class Monstro(Personagem)"""

    def __init__(self, nome, vida, ataque, defesa, recompensa) -> None:
        super().__init__(nome, vida, ataque, defesa)
        self.recompensa = recompensa

    def dar_xp(self, jog: Personagem) -> None:
        """quando o monstro morre, dá o xp dele para o personagem"""
        jog.experiencia += self.recompensa
        print(f"O {jog.nome} ganhou {self.recompensa} de xp.")

    @classmethod
    def cria_esqueleto(cls) -> 'Monstro':
        """cria um monstro esqueleto"""
        return cls("Esqueleto", 50, 10, 2, 100)

    @classmethod
    def cria_goblin(cls) -> 'Monstro':
        """cria um mostro goblin"""
        return cls("Goblin", 20, 8, 1, 20)

    @classmethod
    def cria_diablo(cls) -> 'Monstro':
        """cria o chefe diablo"""
        return cls("Diablo", 250, 25, 8, 1000)

    @staticmethod
    def sorteia_monstro(qtd: int) -> list['Monstro']:
        """cria uma lista de monstros aleatória
        50% de chance de criar um goblin
        40% para o esqueleto
        10 % para o diablo"""
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
            # o jogador ataca o monstro
            self.jogador.atacar(monstro)
            # verifica se o monstro está vivo
            if monstro.vida_atual <= 0:
                print(f"{monstro.nome} foi morto!")
                monstro.dar_xp(self.jogador)
                self.monstros.remove(monstro)
                self.jogador.sobe_level()

                # fim de jogo
                if not self.monstros:
                    break

                # se ainda tiver monstro, pega o próximo aleatório da lista
                monstro = sample(self.monstros, 1)[0]
                print(
                    f"\n---{self.jogador.nome} vai enfrentar {monstro.nome}.---")
            else:
                print(f"{monstro.nome} ainda está vivo.")

            monstro.atacar(self.jogador)
            # verificando se o monstro está vivo ou morto
            if self.jogador.vida_atual <= 0:
                print(f"{self.jogador.nome} foi morto!")
                break
            print(f"{self.jogador.nome} ainda está vivo.")
            print()

        # mostra o status do último monstro
        print(monstro)

    def __str__(self) -> str:
        return 'Board game'
