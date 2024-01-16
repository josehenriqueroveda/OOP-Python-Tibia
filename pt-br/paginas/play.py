import time
from typing import Optional
from random import randint


class Habilidade:
    def __init__(
        self,
        nome: str,
        efeito: str,
        classe: str,
        dano_min: int,
        dano_max: int,
        dano_dot: int,
        duracao_dot: int,
        cura: int,
        summon: Optional[Criatura] = None,
        summon_quantidade: Optional[int] = None,
    ):
        self.nome = nome
        self.efeito = efeito
        self.classe = classe
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.dano_dot = dano_dot
        self.duracao_dot = duracao_dot
        self.cura = cura
        self.summon = summon
        self.summon_quantidade = summon_quantidade

    def curar(self, alvo):
        alvo.hp += self.cura
        print(f"{alvo.nome} foi curado em {self.cura} pontos de vida.")

    def atacar(self, alvo):
        dano = randint(self.dano_min, self.dano_max)
        alvo.hp -= dano
        print(f"{alvo.nome} recebeu {dano} pontos de dano.")

    def ataque_dot(self, alvo):
        alvo.hp -= self.dano_dot
        time.sleep(2)
        print(f"{alvo.nome} recebeu {self.dano_dot} pontos de dano.")
        self.duracao_dot -= 2
        if self.duracao_dot == 0:
            print(f"O efeito de {self.nome} acabou.")
        return

    def invocar_criaturas(self):
        minions = []
        for _ in range(self.summon_quantidade):
            minions.append(self.summon)
        print(f"{self.summon_quantidade} {self.summon} foram invocados.")
        return minions

    def __str__(self):
        return self.nome


class Criatura:
    def __init__(
        self,
        nome,
        hp,
        dificuldade,
        exp,
        ocorrencia,
        velocidade,
        armadura,
        mitigacao,
        habilidades: Habilidade,
        loot,
        vulnerabilidades,
        imunidades,
        pode_ser_puxado,
        empurra_objetos,
        passa_por,
    ):
        self.nome = nome
        self.hp = hp
        self.dificuldade = dificuldade
        self.exp = exp
        self.ocorrencia = ocorrencia
        self.velocidade = velocidade
        self.armadura = armadura
        self.mitigacao = mitigacao
        self.habilidades = habilidades
        self.loot = loot
        self.vulnerabilidades = vulnerabilidades
        self.imunidades = imunidades
        self.pode_ser_puxado = pode_ser_puxado
        self.empurra_objetos = empurra_objetos
        self.passa_por = passa_por

    def __str__(self):
        return self.nome
