import random
from time import sleep

class Monster():
    def __init__(self, name, hp, attack, speed):
        self.state = "normal"
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed

    def attack_to(self,enemy):   
        enemy.hp -= self.attack
        print('%s attacked' % self.name)

    def defence_to(self,enemy):
        self.hp -= enemy.attack / 2
        print('%s defenced' % self.name)

    def chooseAction(self):
        return random.randint(0, 1) 

class Person(Monster):
    def chooseAction(self):
        return int(input('0:attack or 1:defence => '))

class Observer():
    def info(self,object):
        print("%sHP : %d" % (object.name, object.hp))

    def dead(self,object):
        print('%s is dead' % object.name)

    def intro(self,object):
        print('HP:%d, ATTACK:%d, SPEED:%d' %(object.hp, object.attack, object.speed))


def start_battle(obj1:Person,obj2:Person):
    observer = Observer()
    while obj1.hp > 0 and obj2.hp > 0:
        sleep(1)
        obj1_method = obj1.chooseAction()
        obj2_method = obj2.chooseAction() #0 = attack 1= defence
        
        if obj1_method == 0 and obj2_method == 0:
            if obj2.speed <= obj1.speed:
                obj1.attack_to(obj2)
                if obj2.hp <= 0:
                    observer.dead(obj2)
                    break
                observer.info(obj2)
                obj2.attack_to(obj1)
                if obj1.hp <= 0:
                    observer.dead(obj1)
                    break
                observer.info(obj1)
            else:
                obj2.attack_to(obj1)
                if obj1.hp <= 0:
                    observer.dead(obj1)
                    break
                observer.info(obj1)
                obj1.attack_to(obj2)
                if obj2.hp <= 0:
                    observer.dead(obj2)
                    break
                observer.info(obj2)

        elif obj1_method == 0 and obj2_method == 1:
            obj2.defence_to(obj1)
            if obj2.hp <= 0:
                    observer.dead(obj2)
                    break
            observer.info(obj1)
            observer.info(obj2)

        elif obj1_method == 1 and obj2_method == 0:
            obj1.defence_to(obj2)
            if obj1.hp <= 0:
                    observer.dead(obj1)
                    break
            observer.info(obj1)
            observer.info(obj2)

        else:
            print('no attack')






player =  Person('Player', 1000, 100, 100)
player1 =  Person('Player', 1000, 100, 100)
monster = Monster('Monster',random.randint(800, 1200), random.randint(80, 120), random.randint(80, 120))
monster1 = Monster('Monster',random.randint(800, 1200), random.randint(80, 120), random.randint(80, 120))

start_battle(player,player1)