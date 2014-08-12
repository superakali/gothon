from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
			
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
		
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.", 
		"Such a luser.",
		"I have a small puppy that's better at this."
		
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
	
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "Quick on the draw you yan out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laster hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into a rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'
		
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "your head and eats you."
			print 'death'
		
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too qui"
		print "and you need the code to ge the bomb out. If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
　　　　　
			