from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):#scene基类

    def enter(self):
        print("This scene is not yet configured")
        print("Subcladd it and implement enter().")
        exit(1)

class Engine(object):#场景切换引擎
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
# be sure to print out the last scene
            current_scene.enter()

class Death(Scene):#死亡场景

    quips = ["you died.",
            "your mom would be prould",
            "you're worse than your dad's jokes."]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):#初始位置场景
    def enter(self):
        print(dedent("""
                you are running down the central corridor to the weapons"""))

        action = input(">")

        if action == "shoot!":
            print(dedent("""
            then he eat you"""))
            return 'death'

        elif action == "dodge!":
            print(dedent("""like a world class boxer you dodge!"""))
            return 'death'

        elif action == "take a joke":
            print(dedent("""luck for you"""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
                you do a dive roll into the Weapon Armory"""))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BAAAA")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""letting gas out"""))
            return 'the_bridge'

        else:
            print(dedent("""you will die"""))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""you burst onto the bridge"""))

        action = input(">")

        if action == "throw the bomb":
            print(dedent("""when it goes off"""))

            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""you run to the escape pod to get off this"""))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""there are five pod, which one do you take?"""))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""crushing your body into jam jelly."""))
            return 'death'

        else:
            print(dedent("""you jump into pod"""))

            return 'finished'


class Finished(Scene):

    def enter(self):
        print("you won!")
        return 'finished'

class Map(object):
    scenes = {
    'central_corridor':CentralCorridor(),
    'laser_weapon_armory':LaserWeaponArmory(),
    'the_bridge':TheBridge(),
    'escape_pod':EscapePod(),
    'death':Death(),
    'finished':Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
