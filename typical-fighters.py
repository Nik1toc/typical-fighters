



#Everything is made by nik, enjoy ;)

import random

class Character:
    def __init__(self, name, health, knock_out):
        self.name = name
        self.health = health

  # @property
    def is_alive(self):
        return self.health > 0

    def lose(self):
        print(f'{self.name} lost all of his health')


class Monster(Character):
    '''Monster class'''
    
    def __init__(self, name, clasif, weapon, damage, damage_sec, health, stomp, stomp_sec):
        self.damage_sec = damage_sec
        self.stomp_sec = stomp_sec
        self.clasif = clasif
        self.name = name or 'XXX'
        self.weapon = weapon or 'XXX'
        self.damage = random.randint(1,100) if damage < 0 else damage
        self.stomp = random.randint(1,100) if stomp < 0 else stomp
        if health <= 0:
            raise Exception('Error, object health is lower than 0 or equals to 0')
        else:
            self.health = health
    
    def info(self):                              #Information stuff---------
        if self.is_alive():
            print(self.name)
            print(f'Class: {self.clasif}')
            print(f'Weapon: {self.weapon}, damage {self.damage} ')
            if self.name == 'Goblin King':
                print(f'Special move: Stomp {self.stomp} DMG')
            print(f'HP: {self.health}')     
    
    def attack_gk(self, enemy, stomp_check):
        if self.is_alive() and enemy.is_alive():
            if stomp_check:
                if isinstance(enemy, Hero) and not isinstance(enemy, Mage):
                    self.stomp -= enemy.defense
                    self.stomp = 0 if self.stomp < 0 else self.stomp
                enemy.health -= self.stomp
            else:
                if isinstance(enemy, Hero) and not isinstance(enemy, Mage):
                    self.damage -= enemy.defense
                    self.damage = 0 if self.damage < 0 else self.damage
                enemy.health -= self.damage
            if enemy.health < 0:
                enemy.health = 0
            if stomp_check:
                print(f'{self.name} has stomped on {enemy.__class__.__name__} {enemy.name}')
                if self.stomp == self.stomp_sec:
                    print(f'{enemy.name} HP reduced to {enemy.health}\n')
                elif self.stomp != self.stomp_sec and self.stomp != 0 and self.stomp > 0:
                    print(f'{enemy.name} HP reduced to {enemy.health} [{enemy.defense} Blocked]\n')                     
                else:  
                    print(f'{self.name} did no damage [Fully Blocked]\n')
            else:
                print(f'{self.name} has attacked {enemy.__class__.__name__} {enemy.name} with {self.weapon}')
                if self.damage == self.damage_sec:
                    print(f'{enemy.name} HP reduced to {enemy.health}\n')
                elif self.damage != self.damage_sec and self.damage != 0 and self.damage > 0:
                    print(f'{enemy.name} HP reduced to {enemy.health} [{enemy.defense} Blocked]\n') 
                else:
                    print(f'{self.name} did no damage [Fully Blocked]\n')
            print(f'{enemy.name} HP: {enemy.health}\n')
            self.stomp = self.stomp_sec
            self.damage = self.damage_sec
            if enemy.health <= 0:
                enemy.lose()    
    
    def attack_g(self, enemy):
        if self.is_alive() and  enemy.is_alive():
            if isinstance(enemy, Hero) and not isinstance(enemy, Mage):
                self.damage -= enemy.defense
                self.damage = 0 if self.damage < 0 else self.damage
            enemy.health -= self.damage
            if enemy.health < 0:
                enemy.health = 0
            print(f'Monster {self.name} has attacked {enemy.__class__.__name__} {enemy.name} with {self.weapon}')
            if self.damage == self.damage_sec:
                print(f'{enemy.name} HP reduced to {enemy.health}\n')
            elif self.damage < self.damage_sec and self.damage != 0 and self.damage > 0:
                print(f'{enemy.name} HP reduced to {enemy.health} [{enemy.defense} Blocked]\n')                
            else:
                print(f'{self.name} did no damage [Fully Blocked]\n')
            print(f'{enemy.name} HP: {enemy.health}\n')
            self.damage = self.damage_sec
            if enemy.health <= 0:
                enemy.lose()


class Hero(Character):
    '''Main characer'''
    
    def __init__(self, name, clasif, weapon, damage, defense, health, regain, max_health):
        self.clasif = clasif
        self.max_health = max_health
        self.name = name or 'XXX'
        self.weapon = weapon or 'XXX'
        self.damage = random.randint(1,100) if damage <= 0 else damage
        self.defense = random.randint(1,100) if defense <= 0 else defense
        self.regain = random.randint(1,100) if regain <= 0 else regain
        if health <= 0:
            raise Exception('Error, object health is lower than 0 or equals to 0')
        else:
            self.health = health

    def info(self):                              #Information stuff---------
        if self.is_alive() and self.health > 0:
            print(self.name)
            print(f'Class: {self.clasif}')
            print(f'Weapon: {self.weapon}, damage {self.damage} ')
            print(f'Secondary weapon: shield, with {self.defense} defense power ')
            print(f'HP: {self.health}')
            self.defense /= 2                                                     #Doing for defense [Monster.attack]

    def regen(self):
        if self.is_alive():
            self.health += self.regain
            self.health = 100 if self.health >= 100 else self.health
            print(f'Hero {self.name} used health potion')
            print(f'HP increased to {self.health}!')
        
    def attack(self, monst):
        if self.is_alive() and monst.is_alive():
            monst.health -= self.damage
            if monst.health < 0:
                monst.health = 0
            print(f'Hero {self.name} has attacked monster {monst.name} with {self.weapon}')
            print(f'{monst.name} HP reduced to {monst.health}\n')
            if monst.health <= 0:
                monst.lose()


class Mage(Hero):
    '''Based on magic damage'''
    def __init__(self, name, clasif, weapon, health, max_health, fire_ball, ice_spikes, wind_spell):
        self.clasif = clasif
        self.max_health = max_health
        self.name = name or 'XXX'
        self.weapon = weapon or 'XXX'
        self.fire_ball = random.randint(1,100) if fire_ball <= 0 else fire_ball
        self.ice_spikes = random.randint(1,100) if ice_spikes <= 0 else ice_spikes
        self.wind_spell = random.randint(1,100) if wind_spell <= 0 else wind_spell
        if health <= 0:
            raise Exception('Error, object health is lower than 0 or equals to 0')
        else:
            self.health = health
        self.spell_types = {
                    'Fire Ball': self.fire_ball,
                    'Ice Spikes': self.ice_spikes,
                    'Wind Attack': self.wind_spell
                }

    def info(self):                               #Information stuff---------
        if self.is_alive():
            print(self.name)
            print(f'Class: {self.clasif}')
            print(f'Weapon: {self.weapon}')
            print('Spells:') 
            print(f'Fire Ball {self.fire_ball} DMG')         # Fire Ball
            print(f'Ice Spikes {self.ice_spikes} DMG')       # Ice Spikes
            print(f'Wind Attack {self.wind_spell} DMG')     # Wind Attack
            print(f'HP: {self.health}')

    def attack_spell(self, monst, spell_type):
        if self.is_alive() and monst.is_alive():
            monst.health -= self.spell_types.get(spell_type)                          #Senior useful tricks
            if monst.health < 0:
                monst.health = 0
            print(f'Mage {self.name} has attacked monster {monst.name} with {spell_type} spell')
            print(f'{monst.name} HP reduced to {monst.health}\n')
            if monst.health <= 0:
                    monst.lose()


goblin = Monster(
    name='Goblin',
    clasif='Lower goblin class',
     weapon='Club', 
     damage=13,
     damage_sec=13,
     health=100,
     stomp=0,
     stomp_sec=0
)
gking = Monster(
    name='Goblin King',
    clasif='Highest goblin class',
    weapon='Huge Club',
    damage=34,        
    damage_sec=34,
    health=130,
    stomp=38,
    stomp_sec=38
)
hero = Hero(
    name='Emil', 
    clasif='Hero',
    weapon='Holy Sword', 
    damage=26, 
    defense=50, 
    health=100, 
    regain=30,
    max_health=100
)
mage = Mage(
    name='Ronate',
    clasif='Mage',
    weapon='Magic Stuff',
    health=100,
    max_health=100,
    fire_ball=24,
    ice_spikes=27,
    wind_spell=18
)
print('---INTERFACE---')
print('ENEMY TEAM')
gking.info()
print('')
goblin.info()
print('')
print('ALLIES TEAM')
hero.info()
print('')
mage.info()
print('---------------')

def move_gk(stomp_inmove):
    if gking.is_alive():                           
        if hero.is_alive():
            gking.attack_gk(hero, stomp_inmove)
        elif mage.is_alive():
            gking.attack_gk(mage, stomp_inmove)
    move_g()
    
def move_g():
    if goblin.is_alive():
        if hero.is_alive():
            goblin.attack_g(hero)
        elif mage.is_alive():
            goblin.attack_g(mage)
    if not hero.is_alive():
        move_ma()
    else:
        move_h()
    if not mage.is_alive():
        move_h()
    else:
        move_ma()

def move_h():
    while hero.is_alive() and check_monst():
        print('Currently selected: Hero')
        print('Choose one of the moves')
        print(f'---attack({hero.damage} DMG)---regen---change---')
        x = input()                          
        match x:
            case 'attack':
                print('') 
                attack_choose(hero, True)
            case 'regen':
                if hero.max_health != hero.health:
                    print('')
                    hero.regen()
                else:
                    print('Max HP\n')
            case 'change':
                if mage.is_alive():
                    print('')
                    move_ma()
                else:
                    print('Other characters are not available\n')
            case _: 
                print('Error', end='\n')

def move_ma():
    while mage.is_alive() and check_monst():
        print('Currently selected: Mage')
        print('Choose one of the moves')
        print('---attack---change---')
        x = input()
        match x:   
            case 'attack':
                print('') 
                attack_choose(mage, True)
            case 'change':
                if hero.is_alive():
                    print('')
                    move_h()
                else:
                    print('Other characters are not available\n')
            case _: 
                print('Error\n')

def attack_choose(selector, allies_alive):
    while allies_alive and check_monst():
        print('Choose one of the enemies to attack')     #here
        if goblin.is_alive():
            print('--Goblin')
        if gking.is_alive():
            print('--Goblin King')
        print('')
        x = input()
        y = random.randint(1,100)
        if selector == mage:
            match x:
                case 'Goblin':
                    spell_choose(goblin)
                case 'Goblin King':
                    spell_choose(gking)
                case _:
                    print('Error\n')
        else:
            match x:
                case 'Goblin':
                    if goblin.is_alive():
                        hero.attack(goblin)
                        if y > 0 and y < 20:
                            move_gk(True)
                        else:
                            move_gk(False)
                    else:
                        print('Error\n')
                case 'Goblin King':
                    if gking.is_alive():
                        hero.attack(gking)
                        if y > 0 and y < 20:
                            move_gk(True)
                        else:
                            move_gk(False)
                    else:
                        print('Error\n')
                case _:
                    print('Error\n')

def spell_choose(enemy):
    while mage.is_alive() and check_monst():
        print('Choose one of the spells')
        print(f'---Fire Ball({mage.fire_ball} DMG)---Ice Spikes({mage.ice_spikes} DMG)---Wind Attack---({mage.wind_spell} DMG)                -Back')
        x = input()
        y = random.randint(1,100)
        if x in mage.spell_types.keys():
            print('')
            mage.attack_spell(enemy, spell_type=x)
            if y > 0 and y < 20:
                move_gk(True)
            else:
                move_gk(False)
        elif x == 'Back':
            print('')
            move_ma(True)
        else:
            print('Error', end='\n')

def check_monst():
    if gking.is_alive():
        return True
    elif goblin.is_alive():
        return True
    else:
        return False   

move_h()