"""módulo para testar o jogo de rpg"""
from rpg import Game, Guerreiro

conan: Guerreiro = Guerreiro('Conan', 100, 10, 2)
jogo: Game = Game(conan, 150)
jogo.iniciar_luta()
print(conan)
conan.mostra_contagem()
