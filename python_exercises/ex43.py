class Scence(object):
    def enter(self):
        pass
class Engine(object):
    def __init__(self, scene_map):
        pass
    def play(self):
        pass
class Death(Scene):
    def enter(self):
        pass
class EscapePod(Scene):
    def enter(self):
        pass
class Map(object):
    def __inif__(self,start_scene):
        pass
    def next_scene(self,scene_name):
        pass
    def opening_scene(self):
        pass
a_map =Map('central_corridor')
a_game=Engine(a_map)
a_game.play()
