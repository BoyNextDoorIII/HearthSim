import pygame, random
from card import *
from cursor import *
from constants import *
from functions import *


class Player:
    def __init__(self):
        self.__type = 'Player'

        self.__max_health = 30
        self.__health = self.__max_health

        self.__max_mana = 1
        self.__mana = 1

        self.__hand = []

        self.__field = []

        self.__graveyard = []

        self.__deck = []
        self.__fatigue = 0

        self.__mouse = mouse
        self.__holding_pos = None
        self.__attacking_pos = None

        self.__discover_list = []

        self.__holding_card = False
        self.__holding_hero_power = False
        self.__discovering = False
        self.__attacking = False

        self.__spell_damage = 0

        self.import_deck()
        self.draw(4)

    def __str__(self):
        for c in self.__deck:
            print(c.mechanism)

    # get/set hand
    def get_hand(self):
        return self.__hand

    def get_hand_size(self):
        return len(self.__hand)

    def get_hand_index(self, index):
        return self.__hand[index]

    def get_hand_index_cost(self, index):
        return self.__hand[index].get_cost()

    def set_hand_index_cost(self, index, cost):
        self.__hand[index].set_cost(cost)

    def get_hand_index_image(self, index):
        return self.__hand[index].get_image()

    def get_hand_index_type(self, index):
        return self.__hand[index].get_type()

    def hand_add(self, card):
        self.__hand.append(card)

    def remove_hand_index(self, index):
        del self.__hand[index]

    # get/set field
    def get_field(self):
        return self.__field

    def get_field_size(self):
        return len(self.__field)

    def get_field_index(self, index):
        return self.__field[index]

    def get_field_index_attack(self, index):
        return self.__field[index].get_attack()

    def get_field_index_health(self, index):
        return self.__field[index].get_health()

    def get_field_index_image(self, index):
        return self.__field[index].get_image()

    def field_add(self, card):
        self.__field.append(card)

    def field_remove(self, card):
        self.__field.remove(card)

    def remove_field_index(self, index):
        del self.__field[index]

    # get/set deck
    def get_deck(self):
        return self.__deck

    def get_deck_size(self):
        return len(self.__deck)

    def get_deck_index(self, index):
        return self.__deck[index]

    def get_deck_index_family(self, index):
        return self.__deck[index].get_family()

    def get_deck_index_mechanism(self, index):
        return self.__deck[index].get_mechanism()

    def get_deck_index_type(self, index):
        return self.__deck[index].get_type()

    def deck_add(self, card):
        self.__deck.append(card)

    def remove_deck_index(self, index):
        del self.__deck[index]

    # get/set graveyard
    def get_graveyard(self):
        return self.__graveyard

    def get_graveyard_index(self, index):
        return self.__graveyard[index]

    def graveyard_add(self, card):
        self.__graveyard.append(card)

    def remove_graveyard_index(self, index):
        del self.__graveyard[index]

    def graveyard_remove(self, card):
        self.__graveyard.remove(card)

    # get/set others
    def get_attacking_pos(self):
        return self.__attacking_pos

    def set_attacking_pos(self, index):
        self.__attacking_pos = index

    def set_hand_index_targetable(self, index, boolean):
        self.__hand[index].targetable = boolean

    def refresh_mana(self):
        if self.__max_mana < 10:
            self.__max_mana += 1
        self.__mana = self.__max_mana

    def spend_mana(self, amount):
        self.__mana -= amount

    def gain_life(self, amount):
        self.__max_health += amount
        self.__health += amount

    def heal(self, amount):
        self.__health += amount
        if self.__health > self.__max_health: self.__health = self.__max_health

    def is_idle(self):
        return not self.__discovering and not self.__attacking and not self.__holding_card and not self.__holding_hero_power

    def get_spell_damage(self):
        return self.__spell_damage

    def increase_spell_damage(self, amount):
        self.__spell_damage += amount

    # methods
    def set_is_discovering(self, boolean):
        self.__discovering = boolean

    def discover_list_add(self, card):
        self.__discover_list.append(card)

    def discover(cards):
        for i in range(len(cards)):
            SCREEN.blit(cards[i].get_image(), [40, 40 + 50 * i])

    def check_hand(self):
        for i in range(self.get_hand_size()):
            if i > 9:
                self.remove_hand_index(-1)
            elif self.get_hand_index_cost(i) < 0:
                self.set_hand_index_cost(i, 0)

    def combat(self):
        l = self.get_field_size()
        p = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [100, 2])
        if self.__attacking:
            pygame.draw.line(SCREEN, RED, pygame.mouse.get_pos(), [p[0] + (self.get_attacking_pos() - (l - 1) / 2) * 110 + 7+42, p[1]+30+62], 2)
        for i in range(l):
            r = [p[0] + (i - (l - 1) / 2) * 110 + 7, p[1] + 30, 84, 124]
            if self.__mouse.is_on_object(r) and self.__holding_pos == None and self.get_field_index(i).get_can_attack():
                if pygame.mouse.get_pressed()[0] and not self.__mouse.get_is_pressing2():
                    self.__mouse.set_is_pressing2(True)
                    self.set_attacking_pos(i)
                    self.__attacking = True
        if not pygame.mouse.get_pressed()[0] and self.__mouse.get_is_pressing2():
            self.__mouse.set_is_pressing2(False)
            self.__attacking = False
            """attacking_a_minion = False
            l = opponent.get_field_size()
            p = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [100, 2])
            for i in range(l):
                if self.__mouse.is_on_object([p[0] + (i - (l - 1) / 2) * 110, p[1] + 20, 81, 112]):
                    attacking_a_minion = True
                    
                    break"""
            pos_x = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [150, 200])[0]
            if self.__mouse.is_on_object([pos_x, 10, 150, 200]):
                #opponent_take(self.get_field_index_attack(self.__attacking_pos))
                print(self.get_field_index_attack(self.__attacking_pos))
                print(opponent_health)

    def check_targetability(self):
        t_c = ['Topsy_Turvy', 'Power_Word_Shield', 'Divine_Spirit', 'Vivid_Nightmare']
        for c in self.get_hand():
            if c.name in t_c:
                self.set_hand_index_targetable(True)

    def refresh_combat(self):
        for i in range(self.get_field_size()):
            self.get_field_index(i).set_can_attack(True)

    def new_turn(self):
        r = [SCREENWIDTH - 170, (SCREENHEIGHT - 50) / 2, 150, 50]
        if self.__mouse.is_on_object(r):
            if not self.__mouse.get_is_pressing() and pygame.mouse.get_pressed()[0]:
                self.__mouse.set_is_pressing(True)
            elif self.__mouse.get_is_pressing() and not pygame.mouse.get_pressed()[0]:
                self.__mouse.set_is_pressing(False)
                self.begin_turn()
                self.refresh_mana()
                self.refresh_combat()
                self.draw(1)

    def begin_turn(self):
        for m in self.get_field():
            m.beginning_of_turn()

    def print_deck(self):
        for c in self.get_deck():
            print(c.name)

    def import_deck(self):
        f = open("deck.txt", "r")
        d = [x.split() for x in f.readlines()]
        for i in range(len(d)):
            d[i][1] = d[i][1].split(',')
            for x in range(len(d[i][1])):
                d[i][1][x] = int(d[i][1][x])
            d[i][3] = d[i][3].split(',')
        for i in range(len(d)):
            c = Card(d[i][0], d[i][1], d[i][2], d[i][3], d[i][4], self)
            self.deck_add(c)
        self.shuffle()
        f.close()

    def tutor(self, index):
        self.hand_add(self.get_deck_index(index))
        self.remove_deck_index(index)

    def shuffle(self):
        random.shuffle(self.__deck)

    def shuffle_graveyard(self):
        random.shuffle(self.__graveyard)

    def summon_hand_index(self, index):
        self.__field.append(self.__hand[index])

    def play(self, index):
        self.spend_mana(self.get_hand_index_cost(index))
        if self.get_hand_index_type(index) == 'Minion':
            self.summon_hand_index(index)
            self.get_hand_index(index).battlecry()
        elif self.get_hand_index_type(index) == 'Spell':
            l = self.get_field_size()
            p = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [100, 2])
            c = None
            for x in range(self.get_field_size()):
                if self.__mouse.is_on_object([p[0] + (x - (l - 1) / 2) * 110, p[1] + 20, 100, 138]):
                    c = x
            has_target = False
            if c != None:
                target = self.get_field_index(c)
                has_target = True
            if has_target:
                self.get_hand_index(index).effect(target)
            else:
                self.get_hand_index(index).effect()
        self.remove_hand_index(index)

    def take(self, amount):
        self.__health -= amount

    def draw(self, amount):
        for i in range(amount):
            if self.get_deck_size() > 0:
                self.tutor(0)
            else:
                self.__fatigue += 1
                self.take(self.fatigue)

    def enough_mana(self, amount):
        return self.__mana >= amount

    def display_deck_cards(self):
        l = self.get_deck_size()
        t = FONT.render(str(l), True, HONEYDEW)
        p = get_centered([SCREENWIDTH - 145, (SCREENHEIGHT - 50) / 2 + 70, 100, 150], t.get_size())
        SCREEN.blit(t, p)
        if l > 0 and not self.__mouse.is_on_object([SCREENWIDTH - 145, (SCREENHEIGHT - 50) / 2 + 70, 100, 150]):
            SCREEN.blit(CARD_BACK, [SCREENWIDTH - 145, (SCREENHEIGHT - 50) / 2 + 70])

    def display_field_cards(self):
        l = self.get_field_size()
        p = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [100, 2])
        for i in range(l):
            SCREEN.blit(self.get_field_index_image(i), [p[0] + (i - (l - 1) / 2) * 110, p[1] + 20])
            r = [p[0] + (i - (l - 1) / 2) * 110, p[1] + 120, 40, 40]
            pygame.draw.rect(SCREEN, LIGHTYELLOW, r)
            pygame.draw.rect(SCREEN, WHITE, r, 2)
            t = FONT.render(str(self.get_field_index_attack(i)), True, HONEYDEW)
            p2 = get_centered(r, t.get_size())
            SCREEN.blit(t, p2)
            r[0] += 60
            pygame.draw.rect(SCREEN, RED, r)
            pygame.draw.rect(SCREEN, WHITE, r, 2)
            t = FONT.render(str(self.get_field_index_health(i)), True, HONEYDEW)
            p2 = get_centered(r, t.get_size())
            SCREEN.blit(t, p2)
            if self.get_field_index(i).get_can_attack() and self.get_field_index_attack(i) > 0:
                pygame.draw.rect(SCREEN, GREEN, [p[0] + (i - (l - 1) / 2) * 110 + 7, p[1] + 30, 84, 124], 2)

    def display_hand_cards(self):
        for i in range(self.get_hand_size()):
            if i < self.get_hand_size():
                pos_x = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [870, 150])[0]
                rect = [pos_x + i * 85 + 5, SCREENHEIGHT - 164, 91, 134]
                rect2 = [pos_x + i * 85 + 12, SCREENHEIGHT - 154, 84, 124]
                rect3 = list(rect2)
                if self.__mouse.is_on_object(rect2):
                    rect[1] -= 40
                    rect2[1] -= 40
                    if pygame.mouse.get_pressed()[0] and not self.__mouse.get_is_pressing():
                        self.__mouse.set_is_pressing(True)
                        self.__holding_pos = i
                if not pygame.mouse.get_pressed()[0] and self.__mouse.get_is_pressing():
                    self.__mouse.set_is_pressing(False)
                    pos = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [900, 2])
                    pos[1] += 1
                    rect = [pos[0], pos[1], 900, 150]
                    if self.__holding_pos != None:
                        if self.__mouse.is_on_object(rect) and self.enough_mana(self.get_hand_index_cost(self.__holding_pos)):
                            if self.get_hand_index_type(self.__holding_pos) == 'Minion':
                                if self.get_field_size() < 7:
                                    self.play(self.__holding_pos)
                            else:
                                self.play(self.__holding_pos)
                    self.__holding_pos = None
                if i < self.get_hand_size():
                    if self.__holding_pos == i:
                        pos = pygame.mouse.get_pos()
                        x = pos[0]
                        y = pos[1]
                        move(rect, [x - 50, y - 69])
                        move(rect2, [x - 43, y - 59])
                    #if self.get_hand_index(i).get_targetable():
                    #    pygame.draw.line(SCREEN, RED, pygame.mouse.get_pos(), [rect3[0],rect3[1]], 2)
                    #else:
                    SCREEN.blit(self.get_hand_index_image(i), [rect[0], rect[1]])
                    if self.enough_mana(self.get_hand_index_cost(i)):
                        if self.get_hand_index_type(i) == 'Minion':
                            if self.get_field_size() < 7:
                                pygame.draw.rect(SCREEN, GREEN, rect2, 2)
                        else:
                            pygame.draw.rect(SCREEN, GREEN, rect2, 2)
                    r3 = [rect[0], rect[1], 40, 40]
                    pygame.draw.rect(SCREEN, BLUE, r3)
                    pygame.draw.rect(SCREEN, WHITE, r3, 2)
                    t = FONT.render(str(self.get_hand_index_cost(i)), True, HONEYDEW)
                    p = get_centered(r3, t.get_size())
                    SCREEN.blit(t, p)

    def display_health(self):
        x = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [855, 154])[0]
        x = get_centered([0, 0, x, SCREENHEIGHT - 170], [150, 200])[0]
        r = [x + 115, SCREENHEIGHT - 85, 40, 40]
        c = HONEYDEW
        if self.__health < self.__max_health:
            c = ORANGERED
        t = FONT.render(str(self.__health), True, c)
        SCREEN.blit(t, get_centered(r, t.get_size()))

    def display_mana(self):
        x = get_centered([0, 0, SCREENWIDTH, SCREENHEIGHT], [855, 154])[0] + 855
        y = get_centered([x, SCREENHEIGHT - 172, 1280 - x, 172], [104, 104])[1]
        r = [SCREENWIDTH - 147, y, 102, 102]
        t = str(self.__mana) + '/' + str(self.__max_mana)
        t = FONT.render(t, True, HONEYDEW)
        p = get_centered(r, t.get_size())
        SCREEN.blit(t, p)

    def update(self):
        self.__spell_damage = 0
        self.__mouse.update()
        for m in self.get_field():
            if m.get_health() <= 0:
                m.die()
            m.aura()
        self.new_turn()
        self.display_deck_cards()
        self.display_field_cards()
        self.display_health()
        self.display_mana()
        self.check_hand()
        self.display_hand_cards()
        self.combat()
        for c in self.get_hand():
            c.set_cost(c.get_stat()[0])

    def display_hero(self):
        pass
