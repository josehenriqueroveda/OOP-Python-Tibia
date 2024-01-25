# 4 Pillars of OOP

## OOP Basic Principles

At OOP, it is common to talk about the 4 pillars of object-oriented programming: **Abstraction**, **Encapsulation**, **Inheritance** and **Polymorphism**. Let's understand a little more about each of them.

### 1. Abstraction
- **Abstraction:** It is the ability to represent essential characteristics of an object, without representing complex details of its implementation. In Python, abstraction is represented by classes and objects.

- **Class:** A structure that defines the characteristics and behaviors common to a group of objects.
- **Object:** A specific instance of a class, representing a concrete element in the system.
#
### 1.1 Class Attributes and Methods
- **Attribute:** A characteristic of an object, such as its name or color. In Python, attributes are defined within the class's special `__init__` method.

Let's consider a simple Tibia object in Python, a **Torch**. ![Torch](https://www.tibiawiki.com.br/images/9/90/Torch.gif)


It has a **name**, a **weight** and a status of **on** or not.

Its representation in Python would be something like:

```python
class Torch:
     def __init__(self, name, weight, lit):
         self.name = name
         self.weight = weight
         self.lit = lit

torch = Torch('Torch', 5, True)
```

- **Method:** An action that an object can perform, such as turning on or off a torch. In Python, methods are defined within the class.

```python
class Torch:
     def __init__(self, name, weight, lit):
         self.name = name
         self.weight = weight
         self.lit = lit
    
     def turn_on(self):
         self.lit = True
    
     def turn_off(self):
         self.lit = False

# Creating the torch and lighting it
torch = Torch('Torch', 5, False)
torch.turn_on()
```

### 2. Encapsulation
- **Encapsulation:** It is the technique that allows information to be hidden, protecting the data of a class and restricting access to it.

Let's use as an example one of the most common creatures in Tibia, the **Rat**.![Rat](https://www.tibiawiki.com.br/images/a/af/Rat.gif) 

A common creature has a name and HP points. _(For didactic purposes, we will only consider these 2 attributes for now)_.


We can use the concept of encapsulation, making attributes private, that is, accessible only within the class using the `_` prefix and creating methods to access and modify them.

```python
class Creature:
    def __init__(self, name, hp, exp):
        self._name = name
        self._hp = hp
        self._exp = exp
    
    def receive_damage(self, damage):
        self._hp -= damage

# Creating the creature and dealing damage to it
rat = Creature('Rat', 20, 5)
rat.receive_damage(10)
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