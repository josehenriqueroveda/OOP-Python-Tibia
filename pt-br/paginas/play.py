from classes.Criatura import Criatura
from classes.HabilidadeDano import HabilidadeDano
from classes.HabilidadeCura import HabilidadeCura
from classes.HabilidadeEspecial import HabilidadeEspecial
from classes.Loot import Loot
from classes.Resistencia import Resistencia


# Criando as habilidades de dano
corpo_a_corpo = HabilidadeDano(
    nome="Corpo a Corpo",
    descricao="A Giant Spider causa 0-250 pontos de dano físico.",
    tipo="Físico",
    mana=0,
    dano_min=0,
    dano_max=250,
)

poison_field = HabilidadeDano(
    nome="Poison Field",
    descricao="Envenena o solo ao redor do alvo, causando 5 de dano de veneno a cada 2 segundos por 3 minutos. O dano não é afetado pela armadura ou defesa do alvo.",
    tipo="Earth",
    mana=0,
    dano_min=0,
    dano_max=0,
    dano_dot=5,
    duracao_dot=180, # 3 minutos
    intervalo_dot=2,
)

poison_strike = HabilidadeDano(
    nome="Poison Strike",
    descricao="A Giant Spider causa 40-70 pontos de dano do tipo veneno.",
    tipo="Físico",
    mana=0,
    dano_min=40,
    dano_max=70,
)

# Criando as habilidades especiais
summon_spider = HabilidadeEspecial(
    nome="Summon Poison Spider",
    descricao="A Giant Spider pode invocar 1 ou 2 Poison Spiders.",
    mana=0
)

strong_haste = HabilidadeEspecial(
    nome="Strong Haste",
    descricao="A Giant Spider pode aumentar sua velocidade.",
    mana=0
)

# Criando as vulnerabilidades aos tipos de dano
vulnerabilidades = Vulnerabilidade(
    fisico=100,
    fogo=110, # Vulnerável
    gelo=80, # Resistente
    morte=100,
    energia=80, # Resistente
    sagrado=100,
    terra=0, # Imune
    cura=100,
)

# Criando o loot da Giant Spider
gs_loots = [
    Loot(nome="Gold Coin", quantidade=randint(0, 50), chance=1.0),
    Loot(nome="Posion Arrows", quantidade=randint(0, 12), chance=0.25),
    Loot(nome="Plate Armor", quantidade=1, chance=0.25),
    Loot(nome="Plate Legs", quantidade=1, chance=0.25),
    Loot(nome="String Health Potion", quantidade=1, chance=0.08),
    Loot(nome="Spider Silk", quantidade=randint(0, 2), chance=0.08),
    Loot(nome="Steel Helmet", quantidade=1, chance=0.08),
    Loot(nome="Two Handed Sword", quantidade=1, chance=0.08),
    Loot(nome="Knight Armor", quantidade=1, chance=0.03),
    Loot(nome="Knight Legs", quantidade=1, chance=0.03),
    Loot(nome="Time Ring", quantidade=1, chance=0.03),
    Loot(nome="Lightning Headband", quantidade=1, chance=0.01),
    Loot(nome="Platinum Amulet", quantidade=1, chance=0.01)
]

# Criando a Giant Spider
giant_spider = Criatura(
    nome="Giant Spider",
    hp=1300,
    dificuldade="Médio",
    exp=900,
    ocorrencia="Comum",
    velocidade=120,
    armadura=30,
    mitigacao=1.04,
    habilidades_dano=[corpo_a_corpo, poison_field, poison_strike],
    habilidades_cura=[],
    habilidades_especiais=[summon_spider, strong_haste],
    loot=gs_loots,
    vulnerabilidades=vulnerabilidades,
    imunidades=["Veneno", "Paralisia", "Invisibilidade"],
    pode_ser_puxado=False,
    empurra_objetos=True,
    passa_por=["Veneno", "Energia"]
)