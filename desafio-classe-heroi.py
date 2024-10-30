
class action:
    global species
    global weapon 
    def __init__(self, species, weapon):
        self.species = species
        self.weapon = weapon
    def description(self):
        return print(f"O {self.species} atacou usando {self.weapon}!")



def caracterCreate(heroClass):
    global species
    global weapon 
    if choose == 1:
        species = "mago"
        weapon = "magia"
    elif choose == 2:
        species = "guerreiro"
        weapon = "espada"
    elif choose == 3:
        species = "monge"
        weapon = "artes marciais"
    elif choose == 4:
        species = "ninja"
        weapon = "shuriken"
    return species, weapon

choose = int(input("Escolha seu Herói: \n 1-Mago \n 2-Guerreiro \n 3-Monge \n 4-Ninja \n"))

while choose > 4:
    choose = int(input("Escolha seu Herói: \n 1-Mago \n 2-Guerreiro \n 3-Monge \n 4-Ninja \n"))
    break

age = int(input("Qual a idade desse Herói? "))
yourHero = {choose: age}
heroClass = ""
species = ""
weapon = ""

caracterCreate(heroClass)

yourAction = int(input("Deseja atacar?\n 1-Sim \n 2-Não \n"))

while yourAction > 2:
    yourAction = input("Deseja atacar?\n 1-Sim \n 2-Não \n")
    break
if yourAction == 1:
    hero = action(species, weapon)
    
    hero.description()
else:
    print("Você sofreu dano! Use uma poção de cura!")
