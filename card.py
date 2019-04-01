import random
from functions import *

class Card:
    
    def __init__(self, name, stat, card_type, mechanism, family, owner):
        self.__name = name

        self.__image = pygame.image.load("Image\\"+name+".png")

        self.__stat = stat
        self.__cost = stat[0]
        self.__attack = stat[1]
        self.__max_health = stat[2]
        self.__health = stat[2]

        self.__type = card_type

        self.__mechanism = mechanism

        self.__family = family

        self.__can_attack = False

        self.__owner = owner

        self.__targetable = False

        self.__spells_cast = []

        if 'Charge' in self.__mechanism:
            self.__can_attack = True

    def get_owner(self):
        return self.__owner

    def get_name(self):
        return self.__name

    def check_name(self, name):
        return self.__name == name

    def get_image(self):
        return self.__image

    def spells_cast_add(self, card):
        self.__spells_cast.append(card)

    def double_life(self):
        self.__max_health *= 2
        self.__health *= 2

    def gain_life(self, amount):
        self.__max_health += amount
        self.__health += amount

    def heal(self, amount):
        self.__health += amount
        if self.__health > self.__max_health: self.__health = self.__max_health

    def lose(self, amount):
        self.__health -= amount

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def reduce_cost(self, amount):
        self.__cost -= amount

    def get_attack(self):
        return self.__attack

    def set_attack(self, attack):
        self.__attack = attack

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health
        if self.__health > self.__max_health: self.__health = self.__max_health

    def set_max_health(self, health):
        self.__max_health = health
        if self.__health > self.__max_health: self.__health = self.__max_health

    def get_stat(self):
        return self.__stat

    def get_type(self):
        return self.__type

    def get_mechanism(self):
        return self.__mechanism

    def mechanism_remove(self, mech):
        if mech in self.__mechanism:
            self.__mechanism.remove(mech)

    def get_family(self):
        return self.__family

    def get_spells_cast(self):
        return self.__spells_cast

    def set_spells_cast(self, spells):
        self.__spells_cast = spells

    def get_can_attack(self):
        return self.__can_attack

    def set_can_attack(self, boolean):
        self.__can_attack = boolean

    def get_targetable(self):
        return self.__targetable

    # methods
    def effect(self, target=None):
        if target != None:
            target.spells_cast_add(self)
        if self.check_name('Divine_Spirit'):
            target.double_life()
        elif self.check_name('Power_Word_Shield'):
            target.gain_life(2)
            self.get_owner().draw(1)
        elif self.check_name('Psychic_Scream'):
            for i in range(self.get_owner().get_field_size()):
                self.get_owner().deck_add(self.get_owner().get_field_index(0))
                self.get_owner().remove_field_index(0)
            self.get_owner().shuffle()
        elif self.check_name('Shadow_Visions'):
            discovery_list = []
            for i in range(self.get_owner().get_deck_size()):
                if self.get_owner().get_deck_index_type(i) == 'Spell' and self.get_owner().get_deck_index(i) not in discovery_list:
                    discovery_list.append(self.get_owner().get_deck_index(i))
            if len(discovery_list) > 0:
                self.get_owner().set_is_discovering(True)
                if len(discovery_list) >= 3:
                    for i in range(3):
                        random_num = random.randrange(0, len(discovery_list))
                        self.get_owner().discover_list_add(discovery_list[random_num])
                        del discovery_list[random_num]
                elif len(discovery_list) < 3:
                    for i in range(len(discovery_list)):
                        random_num = random.randrange(0, len(discovery_list))
                        self.get_owner().discover_list_add(discovery_list[random_num])
                        del discovery_list[random_num]
        elif self.check_name('Spirit_Lash'):
            for m in self.get_owner().get_field():
                m.take(1+self.get_owner().get_spell_damage())
                self.get_owner().heal(1+self.get_onwer().get_spell_damage())
        elif self.check_name('Topsy_Turvy'):
            health = target.get_health()
            target.set_max_health(target.get_attack())
            target.set_health(target.get_attack())
            target.set_attack(health)
        elif self.check_name("Twilight's_Call"):
            for i in range(2):
                temp_graveyard = list(self.get_owner().get_graveyard())
                random.shuffle(temp_graveyard)
                c = search(temp_graveyard, 'Deathrattle')
                if c != None:
                    c = temp_graveyard[c]
                    temp_graveyard.remove(c)
                    self.get_owner().field_add(c)
                    c.set_attack(1)
                    c.set_max_health(1)
                else:
                    print(False)
        elif self.check_name('Vivid_Nightmare'):
            c = Card(target.get_name(), target.get_stat(), target.get_type(), target.get_mechanism(), target.get_family(), self.get_owner())
            c.set_health(1)
            c.set_attack(int(target.get_attack()))
            c.set_spells_cast(list(target.get_spells_cast()))
            self.get_owner().field_add(c)

    def battlecry(self, target=None):
        if self.check_name('Sandbinder'):
            for i in range(self.get_owner().get_deck_size()):
                if self.get_owner().get_deck_index_family(i) == 'Elemental':
                    self.get_owner().tutor(i)
                    break
        elif self.check_name('Witchwood_Piper'):
            c = 1000
            p = None
            for i in range(self.get_owner().get_deck_size()):
                if self.get_owner().get_deck_index_type(i) == 'Minion':
                    if c > self.get_owner().get_deck_index(i).get_cost():
                        c = self.get_owner().get_deck_index(i).get_cost()
                        p = i
            if p != None:
                self.get_owner().hand_add(self.get_owner().get_deck_index(p))
                self.get_owner().remove_deck_index(p)
        elif self.check_name('Giggling_Inventor'):
            pass

    def deathrattle(self):
        if self.check_name('Test_Subject'):
            for c in self.get_spells_cast():
                self.get_owner().hand_add(c)
        elif self.check_name('Dead_Ringer'):
            for i in range(self.get_owner().get_deck_size()):
                if 'Deathrattle' in self.get_owner().get_deck_index_mechanism(i):
                    self.get_owner().tutor(i)
                    break
        elif self.check_name('Bloodmage_Thalnos'):
            self.get_owner().draw(1)
        elif self.check_name('Loot_Hoarder'):
            self.get_owner().draw(1)

    def aura(self):
        if self.check_name('Radiant_Elemental'):
            for c in self.get_owner().get_hand():
                if c.get_type() == 'Spell':
                    c.reduce_cost(1)
            self.get_owner().check_hand()
        elif self.check_name('Bloodmage Thalnos'):
            self.owner.increase_spell_damage(1)

    def beginning_of_turn(self):
        if self.check_name('Doomsayer'):
            for i in range(self.get_owner().get_field_size()):
                self.get_owner().get_field_index(0).die()

    def die(self):
        self.get_owner().field_remove(self)
        self.deathrattle()
        self.set_spells_cast([])
        self.set_attack(self.get_stat()[1])
        self.set_max_health(self.get_stat()[2])
        self.set_health(self.get_stat()[2])
        self.get_owner().graveyard_add(self)

    def take(self, amount):
        if 'Divine_Shield' in self.get_mechanism():
            self.mechanism_remove('Divine_Shield')
        else:
            self.lose(amount)

    def fight(self, target):
        target.take(self.get_attack())
        if target.type == 'Minion':
            self.take(target.get_attack())
        self.set_can_attack(False)
