# Os 4 Pilares da POO

## Princípios Básicos da POO

Na POO, é comum falarem sobre os 4 pilares da programação orientada a objetos: **Abstração**, **Encapsulamento**, **Herança** e **Polimorfismo**. Vamos entender um pouco mais sobre cada um deles.

### 1. Abstração
- **Abstração:** É a capacidade de representar características essenciais de um objeto, sem representar detalhes complexos de sua implementação. Em Python, a abstração é representada por classes e objetos.

- **Classe:** Uma estrutura que define as características e comportamentos comuns a um grupo de objetos.
- **Objeto:** Uma instância específica de uma classe, representando um elemento concreto no sistema.
#
### 1.1 Atributos e Métodos de Classe
- **Atributo:** Uma característica de um objeto, como seu nome ou cor. Em Python os atributos são definidos dentro do método especial `__init__` da classe.

Vamos considerar um objeto simples do Tibia em Python, uma **Torch**. ![Torch](https://www.tibiawiki.com.br/images/9/90/Torch.gif)


 Ela possui um **nome**, um **peso** e um status de **acesa** ou não.

Sua representação em Python seria algo como:

```python
class Torch:
    def __init__(self, nome, peso, acesa):
        self.nome = nome
        self.peso = peso
        self.acesa = acesa

tocha = Torch('Torch', 5, True)
```

- **Método:** Uma ação que um objeto pode realizar, como acender ou apagar uma tocha. Em Python os métodos são definidos dentro da classe.

```python
class Torch:
    def __init__(self, nome, peso, acesa):
        self.nome = nome
        self.peso = peso
        self.acesa = acesa
    
    def acende(self):
        self.acesa = True
    
    def apaga(self):
        self.acesa = False

# Criando a tocha e acendendo-a
tocha = Torch('Torch', 5, False)
tocha.acende()
```

### 2. Encapsulamento
- **Encapsulamento:** É a técnica que permite a ocultação de informações, protegendo os dados de uma classe e restringindo o acesso a eles.

Vamos utilizar de exemplo um dos criaturas mais comuns do Tibia, o **Rat**. ![Rat](https://www.tibiawiki.com.br/images/a/af/Rat.gif) 

Um criatura comum possui um nome e pontos de HP. _(Para fins didáticos, vamos considerar por enquanto apenas esses 2 atributos)_.



Podemos utilizar o conceito de encapsulamento, tornando os atributos privados, ou seja, acessíveis apenas dentro da classe utilizando o prefixo `_` e criando métodos para acessá-los e modificá-los.

```python
class Criatura:
    def __init__(self, nome, hp, exp):
        self._nome = nome
        self._hp = hp
        self._exp = exp
    
    def receber_dano(self, dano):
        self._hp -= dano

# Criando a criatura e causando dano nela
rat = Criatura('Rat', 20, 5)
rat.receber_dano(10)
```

### 3. Herança
- **Herança:** É a capacidade de criar uma classe a partir de outra classe já existente, herdando seus atributos e métodos.
  
Vamos considerar agora o criatura **Minotaur Mage**. ![Minotaur Mage](https://www.tibiawiki.com.br/images/f/f6/Minotaur_Mage.gif)

Ele possui os mesmos atributos da classe **Criatura**, mas também possui um atributo de _spells_, que é uma lista de magias que ele pode utilizar.

```python
class CriaturaMagica(Criatura):
    def __init__(self, nome, hp, spells):
        super().__init__(nome, hp)
        self._spells = spells

# Criando o Minotaur Mage
minotaur_mage = CriaturaMagica('Minotaur Mage', 155, ['Fireball', 'Great Fireball'])
```

### 4. Polimorfismo
- **Polimorfismo:** É a capacidade de tratar objetos de diferentes tipos de maneira uniforme, através do uso de classes e métodos abstratos. 


Vamos explorar o polimorfismo através de um exemplo prático do Tibia. Consideremos duas classes: 

Um **Jogador**.![Player](https://www.tibiawiki.com.br/images/3/39/Glooth_Bandit.gif) 
```python
class Player:
    def __init__(self, nome, classe, hp, mp, cap, level):
        self._nome = nome
        self._classe = classe
        self._hp = hp
        self._mp = mp
        self._cap = cap
        self._level = level
    
    def atacar(self, alvo, dano):
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self._hp -= dano


# Criando o jogador
player = Player('Darius Calad', 'Knight', 185, 90, 470, 8)
```
E um **Rotworm**.![Rotworm](https://www.tibiawiki.com.br/images/b/b9/Rotworm.gif)

```python
class Criatura:
    def __init__(self, nome, hp, exp):
        self._nome = nome
        self._hp = hp
        self._exp = exp
    
    def atacar(self, alvo, dano):
        alvo.receber_dano(dano)
    
    def receber_dano(self, dano):
        self._hp -= dano

# Criando o Rotworm
rotworm = Commoncriatura('Rotworm', 65, 40)
```

Ambos possuem o método `atacar`, que recebe um alvo e um dano, e chama o método `receber_dano` do alvo.

```python
# O jogador ataca o Rotworm
player.atacar(rotworm, 17)
```

O método `atacar` do jogador recebe o Rotworm como alvo, e chama o método `receber_dano` do Rotworm, que diminui seus pontos de HP.

```python
# O Rotworm ataca o jogador
rotworm.atacar(player, 9)
```

O método `atacar` do Rotworm recebe o jogador como alvo, e chama o método `receber_dano` do jogador, que diminui seus pontos de HP.

## Conclusão

Neste capítulo, aprendemos os princípios básicos da POO, incluindo os conceitos de **Abstração**, **Encapsulamento**, **Herança** e **Polimorfismo**. Esses conceitos são essenciais para o desenvolvimento de aplicações orientadas a objetos, e serão explorados em mais detalhes nos próximos capítulos através de exemplos práticos do Tibia.