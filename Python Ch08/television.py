# Program which simulating TV

class Televisor(object):
	"""TV simulator"""
	def __init__(self, volume = 10):

		self.volume = volume
		
	def change_station(self, station):
		if station == "1":
			print("\nTVP1")
		elif station == "2":
			print("\nTVP2")
		elif station == "3":
			print("\nElven Sports")
		elif station == "4":
			print("\nEskaTv")
		else:
			print("Wrong button. You have only four channels")
			
	def volume_up(self):
		self.volume += 1
		if self.volume > 30:
			self.volume = 30
			print("\nMax volume")
		else:
			print("\nVol:",self.volume)
	
	def volume_down(self):
		self.volume -= 1
		if self.volume < 1:
			self.volume = 0
			print("\nMUTE")
		else:
			print("\nVol:",self.volume)
			
			
def main():
	tele = Televisor()
	print("Welcome in TV simulator")
	choice = None
	while choice != "0":
		print("""

You can choose 1 - 4 buttons to change channel
and + or - to change volume.
To turn off TV press 0.
""")
		choice = input("\nPress button to change channel or volume: ")
		
		# Turn off
		if choice == "0":
			print("Thank you for watching")
			
		# Change channel
		elif choice in ("1", "2", "3", "4"):
			tele.change_station(choice)
		# Turn up volume
		elif choice == "+":
			tele.volume_up()
		# Turn down volume
		elif choice == "-":
			tele.volume_down()

		else: 
			print("Wrong button")

main()
input("\n\nPlease, press enter button to exit game")