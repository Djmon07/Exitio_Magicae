from sys import exit
from random import randint
from textwrap import dedent


class Player(object):
    def __init__(self):
        self.hunger = 50
        self.thirst = 50
        self.food_raw = 0
        self.food_cooked = 5
        self.wood = 0
        self.location = 'string'
        self.mine_equip = False
        self.bow = False
        self.dimonds = 0
        self.coal = 0
        self.gold = 10

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finale')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()


class Scene(object):
    def enter(self):
        exit(1)

    def eat(self):
        if player.food_cooked > 0 and player.hunger != 10:
            print("you eat food")
            player.food_cooked -= 1
            player.hunger += 10

    def stats(self):
        print(dedent(f"""
        Hunger:{player.hunger}
        Thirst:{player.thirst}
        Food:cooked:{food_cooked} raw:{food_raw}
        Wood:{player.wood}
        """))

class Battle(Scene):
    pass
class Game_start(Scene):
    def enter(self):
        print(dedent("""
                Exitio Magicae
            The game of magic death
        """))
        return 'intro'


class Intro(Scene):
    def enter(self):
        choice = input(dedent("""
        :o-|-[
        You awaken to a sound of crumpling leaves.
        infront of you is a man waring a top hat.
        "Hello there my boy I'm sorry to awaken but this is not a charity house"
        you realise that you fell aslep out side the store.
        you apologise to the man and stand up only to get smashed into the wall by a skeloton
        what will you do?
        """))
        if choice == 'fight':
            print('sorry this option is not availible right now so you just die')
            return 'finale'
        elif choice == 'skip':
            print(dedent("""
            you quickly convince the skelotons
            that you are so strong they needent bother
            The mayor then gifts you a cabin in the woods near by as thanks
            you diside to rest for a bit by the magic fire outside"""))
            return 'campfire'


class Campfire(Scene):
    def enter(self):
        choice = input(dedent(f"""
        This is the campfire the fire is lit by a blue atherial fire.
        you see paths to the east north and west.
        there is a cabin behind you
        """))

        if choice == 'east' or choice == 'East':
            print('you take the eastern road')
            player.hunger -= 5
            player.thirst -= 10
            return 'east'
        elif choice == 'north' or choice == 'North':
            print('you take the northern trail')
            player.hunger -= 5
            player.thirst -= 5
            return 'north'
        elif choice == 'West' or choice == 'west':
            print('you take the western path')
            player.hunger -= 5
            player.thirst -= 5
            return 'west'
        elif choice == 'cabin' or choice == 'Cabin':
            print('you go to the cabin')
            return 'cabin'
        elif choice == 'cook' or choice == 'Cook':
            if player.food_raw > 0:
                player.food_raw -= 1
                player.food_cooked += 1
            else:
                print("you do not have any raw food")
            return 'campfire'
        elif choice == 'stats' or choice == 'check':
            self.stats()
            return 'campfire'
        elif str.lower(choice) == 'eat':
            self.eat()
            return 'campfir'
        elif choice == 'quit':
            exit(1)
        else:
            print("you don't know how to do that")
            return 'campfire'


class Cabin(Scene):
    def enter(self):
        choice = input(dedent(f"""
        You enter the cabin. It's old and there is not much inside.
        There is a bed and a fire place
        """))
        if str.lower(choice) == 'cook':
            if player.food_raw > 0:
                player.food_raw -= 1
                player.food_cooked += 1
            else:
                print("you do not have any raw food")
            return 'cabin'
        elif choice == 'rest' or choice == 'Rest':
            print("you sleep")
            return 'cabin'
        elif choice == 'exit' or choice == 'leaves':
            print('you leave the cabin')
            return 'campfire'
        elif choice == 'stats' or choice == 'check':
            self.stats()
            return 'cabin'
        elif str.lower(choice) == 'eat':
            self.eat()
            return 'cabin'
        elif choice == 'quit':
            exit(1)
        else:
            print("no that would be stupid")
            return 'cabin'


class North(Scene):
    def enter(self):
        print(dedent(f"""
        You go down the trail. it goes on for a while.
        eventualy you arive at the a small mining camp.
        """))
        if player.mine_equip == True:
            print('There is a pickaxe and a shovel')
        choice = input("the woods around here look full of deer")
        if str.lower(choice) = 'hunt':
            player.hunger -= 5
            player.thirst -= 5
            if player.bow = True:
                print('You enter the woods with your bow and begin hunting')
                pnumber = input('pick a number 1 through 4')
                random = randint(1,4)
                fnumber = randint(1,3)
                if pnumber == random:
                    player.food_raw += fnumber
                    print(f'you were succesful you gain {fnumber} food')
                    return 'north'
                if pnumber != random:
                    print('you fail to catch anything')
                    return 'north'
        elif str.lower(choice) == 'mine' or str.lower(choice):
            if player.mine_equip == True:
                print ('You venture into the moutain caves and begin to mine')
                mnumber = randint(1,20)
                if mnumber == 20:
                    player.hunger -= 5
                    player.thirst -= 5
                    print('You found a diamond. Congrats!')
                    player.diamonds += 1
                    return 'north'
                elif mnumber > 5:
                    player.hunger -= 5
                    player.thirst -= 5
                    print('You got some coal. Neat!')
                    player.coal += 1
                    return 'north'
                else:
                    player.hunger -= 10
                    player.thirst -= 10
                    print('you found some rocks. be mad')
                    return 'north'
        elif str.lower(choice) == 'pick up' or str.lower(choice) == 'pick up pickaxe':
            if mine_equip == True:
                print('you pickup the shovel and pickaxe and put them on your back')
            else:
                print('you already took them')
            return 'north'

class West(Scene):
    print("no you can't go here... yet im working on it")
    return 'campfire'


class East(Scene):
    def enter(self):
        choice = input(dedent("""
        You enter the town. You see some buildings.
        a blacksmith
        a market
        a well
        """))
        if str.lower(choice) == 'blacksmith':
            print('you go to the blacksmith')
            return 'blacksmith'
        elif str.lower(choice) == 'store' or str.lower(choice) == 'market':
            print ('you go to the market')
            return 'market'
        elif str.lower(choice) == 'well' or  str.lower(choice) == 'go to well':
            fill = input('you go to the well what will you do')
            if str.lower(fill) == 'drink':
                print('you drink some water')
                player.thirst += 1

class Finale(Scene):
    pass


class Map(object):
    scenes = {
        'game_start': Game_start(),
        'intro': Intro(),
        'campfire': Campfire(),
        'cabin': Cabin(),
        'north': North(),
        'west': West(),
        'east': East(),
        'blacksmith': Blacksmith(),
        'market': Market(),
        'well': Well(),
        'finale': Finale()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


player = Player()
a_map = Map('campfire')
a_game = Engine(a_map)
a_game.play()
