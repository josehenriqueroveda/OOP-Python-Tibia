# Implementação Prática III - Criando a Classe Personagem

Finalmente, chegou a última parte da nossa implementação prática. Nesta seção, vamos criar a classe `Personagem` e implementar os seus atributos e métodos.

Para identificar os atributos e métodos da classe `Personagem`, vamos analisar as características e comportamentos que definem um personagem no Tibia a partir de uma perspectiva orientada a objetos, observando a imagem abaixo:

![Personagem](https://www.tibiawiki.com.br/images/e/e0/Gladiator.gif)

A partir dessa imagem, (*de forma simplificada*) podemos identificar os seguintes atributos e métodos:
- **Atributos:**
    - `nome`
    - `hp`
    - `mana`
    - `level`
    - `experiencia`
    - `capacidade`
    - `itens_equipados`
    - `magic_level`
    - `sword_fighting`
    - `axe_fighting`
    - `club_fighting`
    - `distance_fighting`
    - `shielding`
    - `fishing`
    - `fist_fighting`
  

- **Métodos:**
  - `atacar`
  - `receber_dano`
  - `usar_item`
  - `usar_magia`
  - `ganhar_experiencia`
  - `ganhar_level`


## Criando a Classe Personagem

Indetificamos os atributos e métodos da classe `Personagem`, porém antes de implementá-los, algumas classes auxiliares serão criadas, como `Item` e `Magia`.

A classe `Item` que iremos utilizar é a mesma da [Implementação Prática I]().
```python
class Item:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def __str__(self):
        return f"You see a {self.nome}. It weighs {self.peso} oz."
```

A classe `Magia` será criada para representar as magias do personagem no Tibia. A classe `Magia` possui os seguintes atributos:
- `nome`
- `custo`
- `cooldown`
- `premium`

E os seguintes métodos:
- `usar`

A classe `Magia` ficará assim:
```python
class Magia:
    def __init__(self, nome: str, tipo: str, custo: int, cooldown: float, usada_por: str, nivel_min: int, premium=bool):
        self.nome = nome
        self.tipo = tipo
        self.custo = custo
        self.cooldown = cooldown
        self.usada_por = usada_por
        self.nivel_min = nivel_min
        self.premium = premium


    def usar(self):
        print(f"Você usou a magia {self.nome}.")
```

No tibia existem vários tipos de magias, de ataque, de cura, de suporte, de suprimentos e de summon. Para simplificar a implementação, vamos considerar apenas as magias de **ataque** e **cura** que são as mais comuns.

Então, vamos criar duas classes que herdam da classe `Magia`: `MagiaAtaque` e `MagiaCura`.

A classe `MagiaAtaque` possui os seguintes atributos:
- `dano`
- `area`

E a classe `MagiaCura` possui os seguintes atributos:
- `cura`
- `area`

As classes `MagiaAtaque` e `MagiaCura` ficarão assim:
```python
class MagiaAtaque(Magia):
    def __init__(self, nome: str, tipo: str, custo: int, cooldown: float, usada_por: str, nivel_min: int, premium=bool, dano: int, area: bool):
        super().__init__(nome, tipo, custo, cooldown, usada_por, nivel_min, premium)
        self.dano = dano
        self.area = area


class MagiaCura(Magia):
    def __init__(self, nome: str, tipo: str, custo: int, cooldown: float, usada_por: str, nivel_min: int, premium=bool, cura: int, area: bool):
        super().__init__(nome, tipo, custo, cooldown, usada_por, nivel_min, premium)
        self.cura = cura
        self.area = area
```

Agora que criamos as classes `Item` e `Magia`, podemos criar a classe `Personagem`.

A classe `Personagem` completa assim:
```python
from classes.item import Item
from classes.magia import Magia, MagiaAtaque, MagiaCura


class Personagem:
    def __init__(self, nome: str, classe: str, hp: int, mana: int, level: int, experiencia: int, capacidade: int, itens_equipados: list, magic_level: int, sword_fighting: int, axe_fighting: int, club_fighting: int, distance_fighting: int, shielding: int, fishing: int, fist_fighting: int):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        self.mana = mana
        self.level = level
        self.experiencia = experiencia
        self.capacidade = capacidade
        self.itens_equipados = itens_equipados
        self.magic_level = magic_level
        self.sword_fighting = sword_fighting
        self.axe_fighting = axe_fighting
        self.club_fighting = club_fighting
        self.distance_fighting = distance_fighting
        self.shielding = shielding
        self.fishing = fishing
        self.fist_fighting = fist_fighting

    
    def atacar(self, alvo, dano):
        print(f"Você atacou {alvo.nome} e causou {dano} hitpoints de dano.")
        alvo.hp -= dano
    
    def receber_dano(self, dano, tipo):
        if tipo == "físico":
            print(f"Você recebeu {dano - self.shielding} hitpoints de dano.")
            self.hp -= (dano - self.shielding)
        else:
            print(f"Você recebeu {dano} hitpoints de dano.")
            self.hp -= dano
    
    def usar_item(self, item):
        print(f"Você usou o item {item.nome}.")

    
    def usar_magia(self, magia, alvo):
        print(f"Você usou a magia {magia.nome} em {alvo.nome}.")
        if magia.isinstance(MagiaAtaque):
            alvo.receber_dano(magia.dano, magia.tipo)
        elif magia.isinstance(MagiaCura):
            self.hp += magia.cura
    
    def ganhar_experiencia(self, experiencia):
        print(f"Você ganhou {experiencia} pontos de experiência.")
        self.experiencia += experiencia
    
    def ganhar_level(self):
        print(f"Você ganhou um level.")
        self.level += 1
        if self.classe == "Knight":
            self.hp += 15
            self.mana += 5
            self.capacidade += 25
        elif self.classe == "Paladin":
            self.hp += 10
            self.mana += 15
            self.capacidade += 20
        elif self.classe == "Sorcerer":
            self.hp += 5
            self.mana += 30
            self.capacidade += 10
        elif self.classe == "Druid":
            self.hp += 5
            self.mana += 30
            self.capacidade += 10
```

Pronto, agora temos a classe `Personagem` completa. Vamos testar a nossa classe `Personagem` criando um personagem e executando alguns métodos.

```python
from classes.personagem import Personagem
from classes.item import Item
from classes.magia import Magia, MagiaAtaque, MagiaCura

set_equipado = [Item("Steel Helmet", 46), Item("Plate Armor", 120), Item("Plate Legs", 50), Item("Leather Boots", 9), Item("Orcish Axe", 45), Item("Dwarven Shield", 55), Item("Axe Ring", 1), Item("Scarf", 2)]

# Criando um personagem
personagem = Personagem("Darius Calad", "Knight", 185, 90, 8, 5230, 470, set_equipado, 3, 21, 65, 14, 11, 64, 50, 10)

```

Agora vamos executar alguns métodos do personagem.

```python
# Atacando um Rotworm
>>> rotworm = Criatura("Rotworm", 65, 40)
>>> personagem.atacar(rotworm, 17)
Você atacou Rotworm e causou 17 hitpoints de dano.

# Usando um item
>>> item = Item("Health Potion", 2)
>>> personagem.usar_item(item)
Você usou o item Health Potion.

# Usando uma magia
>>> magia = MagiaAtaque("Exori", "físico", 20, 2.5, "Knight", 8, False, 30, False)
>>> personagem.usar_magia(magia, rotworm)
Você usou a magia Exori em Rotworm.

# Recebendo dano
>>> personagem.receber_dano(9, "físico")
Você recebeu 4 hitpoints de dano.

# Ganhar experiência
>>> personagem.ganhar_experiencia(100)
Você ganhou 100 pontos de experiência.

# Ganhar level
>>> personagem.hp = 185
>>> personagem.mana = 90
>>> personagem.capacidade = 470

>>> personagem.ganhar_level()
Você ganhou um level.

>>> personagem.hp
200
>>> personagem.mana
95
>>> personagem.capacidade
495
```

## Conclusão

Nesta seção, criamos a classe `Personagem` e implementamos os seus atributos e métodos. Agora, temos uma classe que representa um personagem no Tibia, e que pode ser utilizada para criar personagens e executar ações como atacar, usar itens e magias, receber dano, ganhar experiência e ganhar level.



