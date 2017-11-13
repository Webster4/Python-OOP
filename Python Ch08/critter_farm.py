# Program basedn on OOP 
# Your are a critter farm keeper
# You have to carry out your pupils
# You can determine amount of pupils in your farm
# You have to carry out of each pupil who is different 

import random

class Critter(object):
	"""Virtual pupil"""
	def __init__(self, name, boredom = random.randint(0, 7), hunger = random.randint(0, 7)):
		self.name = name
		self.boredom = boredom
		self.hunger = hunger
	
	def __str__(self):
		rep = 'Name: {}\nBoredom: {}\nHunger: {}'.format(self.name,
																		self.boredom,
																		self.hunger) 
		return rep
	
	def __pass_time(self):
		self.boredom += 1
		self.hunger += 1
		
	@property
	def mood(self):
		unhappiness = self.boredom + self.hunger
		
		if unhappiness <= 5:
			m = "happy"
			
		elif 5 < unhappiness <=10:
			m = "glad"
		
		elif 10 < unhappiness <=15:
			m = "overstrung"
			
		elif unhappiness > 15:
			m = "pissed"
		
		return m
	
	# Listen your pupil
	def talk(self):
		print("\nMy name is",self.name,". I feel", self.mood)
		self.__pass_time()
		
	# Feed pupil	
	def eat(self, feed = 4):
		# Checking if gave a number
		while True:
			try:
				feed = int(input("\nHow much food do you want to give your pupil {}? ".format(self.name)))
				break
			except ValueError as e:
				print(e)
		self.hunger -= feed
		print("\nThank you for a meal")
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()
	
	# Play with pupil
	def play(self, fun = 4):
		# Checking if gave a number
		while True:
			try:
				fun = int(input("\nHow much time do you want to spare for fun with critter {}? ".format(self.name)))
				break
			except ValueError as e:
				print(e)
		self.boredom -= fun
		print("\nYuuupiii! ;)")
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()
		

def main():
	# Creating objects
	while True:
		try:
			num = int(input("Please give a number of criters: "))
			break
		except ValueError as e:
			print(e)
		
	crit_list =[]
	
	for crit in range(num):
		crit_name = input("Please enter the name of your virtual pupil {}: ".format(crit+1))
		crit = Critter(crit_name)
		crit_list.append(crit)
	
	# Menu
	choice = None
	while choice != "0":
		print(
		"""
		You have to carry out your pupil.

		0 - Exit the game
		1 - Listen what beastie wanna say
		2 - Feed beastie
		3 - Let's play with beastie
		""")
		
		choice = input("\n\nWhat you gonna do? ")
		
		if choice == "0":
			print("\n\nThank you for your time. Good bye")
			
		elif choice == "1":
			for crit in crit_list:
				crit.talk()
		# Feeding critter	
		elif choice == "2":
			for crit in crit_list:
				crit.eat()
		# Fun with critter
		elif choice == "3":
			for crit in crit_list:
				crit.play()
		# Print out an object		
		elif choice == "i":
			for critter in crit_list:
			print(crit)
		# Number out of range
		else:
			print("\nYou've enter wrong number")
			
# Initialize program
main()			
input("\n\nPlease, press enter button to exit game")