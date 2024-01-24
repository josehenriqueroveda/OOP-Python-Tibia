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
  - `defender`
  - `usar_item`
  - `usar_magia`
  - `ganhar_experiencia`
  - `ganhar_level`


## Criando a Classe Personagem

Agora que já identificamos os atributos e métodos da classe `Personagem`, podemos criar a classe em si. Para isso, vamos criar um arquivo chamado `personagem.py` na pasta `classes` e adicionar o seguinte código:

```python
class Personagem:
    pass
```
