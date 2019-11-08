import random

class Hero:
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level
    
    def upLevel(self):
        self.level += 1


class Soldier:
    def __init__(self, number):
        self.number = number

    def goToHero(self, hero):
        return f'{self.number} иду за {hero.name}'

Gazgyl_mak_uruk_traka = Hero('AntiMag')
linus_torvalts = Hero('Avatar')

teamRed = []; teamBlue = []

for _ in range(100):
    number = random.random()

    if number < 0.55555555555555555:
        soldierBlue = Soldier(_)
        teamBlue.append(soldierBlue)

    elif number > 0.55555555555555555:
        soldierRed = Soldier(_)
        teamRed.append(soldierRed)

teamSoldierRed = random.randint(0, teamRed.__len__() - 1)
teamSoldierBlue = random.randint(0, teamBlue.__len__() - 1)

print(teamBlue.__len__(), teamRed.__len__())
print(teamSoldierBlue, teamSoldierRed)

gazgyl = teamBlue[teamSoldierRed].goToHero(Gazgyl_mak_uruk_traka)
linus = teamRed[teamSoldierBlue].goToHero(linus_torvalts)

if teamRed.__len__() > teamBlue.__len__():
    Gazgyl_mak_uruk_traka.upLevel()

    print(gazgyl)
    print(f'Уровень {Gazgyl_mak_uruk_traka.name}:', Gazgyl_mak_uruk_traka.level)

elif teamBlue.__len__() > teamRed.__len__():
    linus_torvalts.upLevel()

    print(linus)
    print(f'Уровень {linus_torvalts.name}: ',linus_torvalts.level)

else:
    Gazgyl_mak_uruk_traka.upLevel()
    print(gazgyl)
    print(f'Уровень {Gazgyl_mak_uruk_traka.name}:', Gazgyl_mak_uruk_traka.level)

    linus_torvalts.upLevel()
    print(linus)
    print(f'Уровень {linus_torvalts.name}: ',linus_torvalts.level)
