# Program basedn on OOP 
# Your are a critter keeper
# You have to carry out your pupil

class Critter(object):
	"""Virtual pupil"""
	def __init__(self, name, boredom = 0, hunger = 0):
		self.name = name
		self.boredom = boredom
		self.hunger = hunger
	
	def __str__(self):
		rep = 'Name: ' + self.name + '\n' + 'Hunger: ' \
		+ str(self.hunger) + '\n' 'Boredom: ' \
		+ str(self.boredom) + '\n'
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
		if feed > 10:
			self.hunger = 0
			print(self.name, "is overfed but he is the most happiest on the world")
		elif feed > 4:
			self.hunger -= feed+2
			print("\nYummy yummy!", self.name, "enjoy that :)")
		else:
			self.hunger -= feed
			print("\nThank you for a meal")
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()
	
	# Play with pupil
	def play(self, fun = 4):
		if fun > 10:
			self.boredom = 0
			print("\nYooohooo! What a fun!!!")
		elif fun > 4:
			self.boredom -= fun+2
			print("\nYuupii! I'm really enjoy!!!")
		else:
			self.boredom -= fun
			print("\nI'm little bit less borring now ;)")
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()
		

def main():
	# 
	crit_name = input("Please enter the name of your virtual pupil: ")
	crit = Critter(crit_name)
	
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
			crit.talk()
		# Feeding critter	
		elif choice == "2":
			food = input("\nHow much food do you want to give your pupil? ")
			if food:
				crit.eat(int(food))
			else:	
				crit.eat()
		# Fun with critter
		elif choice == "3":
			time = input("\nHow much time do you want to spare for fun with critter? ")
			if time:
				crit.play(int(time))
			else:
				crit.play()
		elif choice == "i":
			print(crit)
		else:
			print("\nYou've enter wrong number")
			
# Initialize program
main()			
input("\n\nPlease, press enter button to exit game")