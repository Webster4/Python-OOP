# Program basedn on OOP 
# Your are a critter keeper
# You have to carry out your pupil

class Critter(object):
	"""Virtual pupil"""
	def __init__(self, name, boredom = 0, hunger = 0):
		self.name = name
		self.boredom = boredom
		self.hunger = hunger
		
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
		print("My name is", self.name, ". I feel", self.mood)
		self.__pass_time()
		
	# Feed pupil	
	def eat(self, feed = 4):
		print("Yummy yummy, thank you")
		self.hunger -= feed
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()
	
	# Play with pupil
	def play(self, fun = 4):
		print("Yupi!!!")
		self.boredom -= fun
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
		
		choice = input("What you gonna do? ")
		
		if choice == "0":
			print("Thank you for your time. Good bye")
			
		elif choice == "1":
			crit.talk()
			
		elif choice == "2":
			crit.eat()
			
		elif choice == "3":
			crit.play()
			
		else:
			print("\nYou've enter wrong number")
			
# Initialize program
main()			
input("\n\nPlease, press enter button to exit game")