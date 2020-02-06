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
        self.diamonds = 0
        self.coal = 0
        self.gold = 10
        self.canteen = 0
        self.water = 0
class Admin(object):
    def __init__(self):
        self.hunger = 100
        self.thirst = 50
        self.food_raw = 100
        self.food_cooked = 100
        self.wood = 100
        self.location = 'string'
        self.mine_equip = False
        self.bow = False
        self.diamonds = 100
        self.coal = 100
        self.gold = 10000000
        self.canteen = 1000
        self.water = 1000
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
        if player.food_cooked > 0:
            if player.hunger > 200:
                print("you eat food")
                player.food_cooked -= 1
                player.hunger += 10
            else:
                print('you are full')

    def stats(self):
        print(dedent(f"""
        gold: {player.gold}
        Hunger:{player.hunger}
        Thirst:{player.thirst}
        Food:cooked:{player.food_cooked} raw:{player.food_raw}
        Wood:{player.wood}
        diamonds: {player.diamonds}
        coal:{player.coal}
        """))
        if player.canteen == True:
            print(f'Canteen: {player.water}')


class Battle(Scene):
    pass


class Game_start(Scene):
    def enter(self):
        print(dedent("""
                Exitio Magicae
            The game of magic death
                    start
                    info
                    quit
        """))
        chose = input()
        if str.lower(chose) == 'start':
            print('Game Start')
            return 'intro'
        elif str.lower(chose) == 'quit':
            print('y')
            exit(1)
        elif str.lower(chose) == 'info':
            print(dedent("""
            you can type thease comands at any time:
            eat
            stats
            quit

            """))
        return 'game_start'

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
            return 'death'
        elif choice == 'skip':
            print(dedent("""
            you quickly convince the skelotons
            that you are so strong they needent bother
            The mayor then gifts you a cabin in the woods near by as thanks
            you diside to rest for a bit by the magic fire outside"""))
            return 'campfire'
        else:
            print('wot')
            return 'intro'
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
            return 'campfire'
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
        the woods around here look full of deer
        """))
        if player.mine_equip == False:
            print('There is a pickaxe and a shovel')
        choice = input()
        if str.lower(choice) == 'hunt':
            player.hunger -= 5
            player.thirst -= 5
            if player.bow == True:
                print('You enter the woods with your bow and begin hunting')
                pnumber = input('pick a number 1 through 4')
                random = randint(1, 4)
                fnumber = randint(1, 3)
                if pnumber == random:
                    player.food_raw += fnumber
                    print(f'you were succesful you gain {fnumber} food')
                if pnumber != random:
                    print('you fail to catch anything')
                return 'north'
            else:
                print('you dont have a bow and cant hunt.')
                return 'north'
        elif str.lower(choice) == 'mine':
            if player.mine_equip == True:
                print('You venture into the moutain caves and begin to mine')
                mnumber = randint(1, 20)
                if mnumber == 20:
                    player.hunger -= 5
                    player.thirst -= 5
                    print('You found a diamond. Congrats!')
                    player.diamonds += 1

                elif mnumber > 5:
                    player.hunger -= 5
                    player.thirst -= 5
                    print('You got some coal. Neat!')
                    player.coal += 1

                else:
                    player.hunger -= 10
                    player.thirst -= 10
                    print('you found some rocks. be mad')
            else:
                print('you do not have a pick')
            return 'north'
        elif str.lower(choice) == 'pick up' or str.lower(choice) == 'pick up pickaxe':
            if player.mine_equip == False:
                print('you pickup the shovel and pickaxe and put them on your back')
                player.mine_equip = True
                return 'north'
            else:
                print('you already took them')
                return 'north'
        elif str.lower(choice) == 'back' or str.lower(choice) == 'leave':
            print('you return to your fire')
            return 'campfire'
        elif str.lower(choice) == 'stats':
            self.stats()
            return 'north'
        else:
            print('not an option')
            return 'north'


class West(Scene):
    def enter(self):
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
            print('you go to the market')
            return 'market'
        elif str.lower(choice) == 'well' or str.lower(choice) == 'go to well':
            print('you walk to the well')
            return 'well'
        elif str.lower(choice) == 'stats':
            self.stats()
            return 'east'
        elif str.lower(choice) == 'eat':
            self.eat()
            return 'east'
        elif str.lower(choice) == 'quit':
            exit(1)

        else:
            print("thats not a great thing to do")
            return 'east'
class Well(Scene):
    def enter(self):
        print('you arive at the well what will you do')
        fill = input()
        if str.lower(fill) == 'drink':
            if player.thirst < 100:
                print('you drink some water')
                while player.thirst < 100:
                    player.thirst += 1
                return 'well'
        elif str.lower(fill) == 'fill':
            if player.canteen > 0:
                print('you use the well to fill your canteen')
                while player.water < player.canteen:
                    player.water += 1
                return 'well'
            else:
                print('you dont own a canteen')
                return 'well'
        elif str.lower(fill) == 'leave':
            print('you go back to town square')
            return 'east'
        else:
            print('eather drink fill or just leave')
            return 'well'


class Market(Scene):
    def enter(self):
        choice = input(dedent("""
        you enter the market and go to a stall
        he has some items out for sail
        an apple(1 cooked food): 5g
        Meat(3 cooked food): 10g
        health potion: 1000000g
        """))
        if str.lower(choice) == 'apple' or str.lower(choice) == 'buy apple':
            if player.gold >= 5:
                player.gold -= 5
                player.food_cooked += 1
                print('you buy an apple')
            else:
                print('you need more gold')
            return 'market'
        elif str.lower(choice) == 'meat' or str.lower(choice) == 'buy meat':
            if player.gold >= 10:
                player.gold -= 10
                player.food_cooked += 3
                print("you buy some meat")
            else:
                print('you need more gold')
            return 'market'
        elif str.lower(choice) == 'health potion' or str.lower(choice) == 'buy health potion':
            if player.gold >= 10:
                player.gold -= 10
                player.food_cooked += 100000000000
                print("this doesn't do anything yet so please enjoy the infinite food")
            else:
                print('no')
            return 'market'
        elif str.lower(choice) == 'leave':
            print('you go back to the square')
            return 'east'
        elif str.lower(choice) == 'stats':
            self.stats()
            return 'east'
        elif str.lower(choice) == 'eat':
            self.eat()
            return 'east'
        elif str.lower(choice) == 'quit':
            exit(1)
        else:
            print('no thats not right')
            return 'east'

class Blacksmith(Scene):
    def enter(self):
        choice = input(dedent(f"""
        you enter the blacksmith.
        As you enter the blacksmith smiles warmly and asks
        "what can I do you for"
        he layes out his wares with the prises attached
        upgraid canteen(capacity {player.canteen + 10}):100g
        Bow(lets you hunt): 300g
        it also has a note that saids he will buy any gems or coal off you
        """))
        if str.lower(choice) == 'canteen' or str.lower(choice) == "buy canteen":
            if player.gold >= 100:
                player.gold -= 100
                player.canteen += 10
                print(dedent("""you buy a upgraid to your canteen.
                Its the same size some how and you have no clue how on earth that works.
                The blacksmith just winks at you"""))
            else:
                print('not enough money')
            return 'market'
        elif str.lower(choice) == 'bow' or str.lower(choice) == "buy bow":
            if player.bow == True:
                print('you already have one')
            elif player.gold >= 300:
                player.gold -= 300
                player.bow = True
                print('you now have a bow. Now go hunt.')
            else:
                print('not enough money')
            return 'market'
        elif str.lower(choice) == 'sell':
            print('what would you like to sell')
            minaral = input()
            if str.lower(minaral) == 'diamond' or str.lower(minaral) == 'diamonds' :
                if player.diamonds > 0:
                    player.diamonds -= 1
                    player.gold += 100
                    print('you sell a diamond ')
                else:
                    print('YOU HAVE NOT ENOUGH MINARALS')

            elif str.lower(minaral) == 'coal':
                if player.coal > 0:
                    player.coal -= 1
                    player.gold += 10
                    print('you sell coal for 10 gold')
                else:
                    print('YOU HAVE NOT ENOUGH MINARALS')
            else:
                print('thats not a minaral')
            return 'blacksmith'

        elif str.lower(choice) == 'stats':
            self.stats()
            return 'east'
        elif str.lower(choice) == 'eat':
            self.eat()
            return 'east'
        elif str.lower(choice) == 'quit':
            exit(1)
        else:
            print('no thats not right')
            return 'east'

class Finale(Scene):
    pass


class Death(Scene):
    def enter(self):
        choice = input(dedent("""
        you have died not bit suprise
        Play Again?
        """))
        if str.lower(choice) == 'yes' or str.lower(choice) == 'play again':
            player = Player()
            return 'into'
        if str.lower(choice) == 'no' or str.lower(choice) == 'quit':
            quit(1)
        else:
            print('what')
            return 'death'


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
        'death': Death(),
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
a_map = Map('game_start')
a_game = Engine(a_map)
a_game.play()
