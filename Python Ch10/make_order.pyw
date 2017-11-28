# Program which helps you make an order
# Based on GUI interface
# Program collects all order's item and calculat price

from tkinter import *

class Application(Frame):
    """GUI app which helps make an order in easier way"""
    def __init__(self, master):
        """Initialize of frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        Creating widgets necessary to make correct order
        """
        # List of pizzas
        pizzas = [["Margherita", 13.50, 20.00, 25.00],
                  ["Capriciosa", 14.50, 21.00, 26.00],
                  ["Diavolo", 15.50, 22.00, 27.00],
                  ["Cheesy", 14.00, 21.50, 24.50],
                  ["Special", 17.50, 23.00, 28.50]]

        # First title label
        Label(self, text = "MENU", fg='red').grid(row = 0, column = 3, columnspan = 2)

        # Label for pizzas
        Label(self, text = "Pizza").grid(row = 3, column = 0)
        Label(self, text = "        ").grid(row = 3, column = 3)

        # Label for price and size
        Label(self, text = "Price/size").grid(row = 2, column = 5)
        Label(self, text = "30 cm").grid(row = 3, column = 4)
        Label(self, text = "40 cm").grid(row = 3, column = 5)
        Label(self, text = "50 cm").grid(row = 3, column = 6)

        # Creating list of IntVar class objects
        self.func_name = []
        for i in range(len(pizzas)*3):
            self.func_name.append("is_price"+str(i))
            self.func_name[i] = IntVar()

        # Creating checkbox to mark your pizza and list of prices to adding it in text area
        row = 4
        i = 0
        self.prices = []
        for pizza in pizzas:
            Label(self, text = pizza[0]).grid(row = row, column = 0)
            Checkbutton(self,
                        text = pizza[1],
                        variable = self.func_name[0+i]
                        ).grid(row = row, column = 4, sticky = W)
            Checkbutton(self,
                        text = pizza[2],
                        variable = self.func_name[1+i]
                        ).grid(row = row, column = 5, sticky = W)
            Checkbutton(self,
                        text = pizza[3],
                        variable = self.func_name[2+i]
                        ).grid(row = row, column = 6, sticky = W)

            for price in pizza:
                if type(price) != str:
                    self.prices.append(price)

            row +=1
            i += 3

        # Creating button of order confirmation
        Button(self,
               text = "Confirm order",
               command = self.sum_order
               ).grid(row = 9, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 2, wrap = WORD)
        self.story_txt.grid(row = 10, column = 0, columnspan = 7)


    def sum_order(self):
        """Displaying in text area summary bill"""
        info = "Your bill is: "
        i = 0
        total = 0
        # Getting value from GUI interface
        for func in self.func_name:
            if func.get():
                total += self.prices[i]

            i+=1

        info += str(total)
        info += " $"


        # Displaying total bill
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, info)


# Main part
root = Tk()
root.title("MENU")
app = Application(root)
root.mainloop()
