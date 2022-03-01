# Javier -------------------------------------------------------------------------
import tkinter as tk
from PIL import Image, ImageTk
import random

from settings import Settings
# Javier -------------------------------------------------------------------------

# Jean ---------------------------------------------------------------------------
class Window(tk.Tk) :
	def __init__(self, app) :
		super().__init__()
		self.app = app
		self.settings = app.settings
 
		self.geometry(self.settings.app_geometry)
		self.title(self.settings.app_title)

		self.button = tk.Button(self, text="Roll Dice", command=self.roll_dice)
		self.button.grid(row=0, column=0, columnspan=2)
# Jean ---------------------------------------------------------------------------
# Nadya --------------------------------------------------------------------------
	def roll_dice(self) :
		path1 = random.choice(self.settings.dice_path)
		path2 = random.choice(self.settings.dice_path)

		self.fotoDadu = ImageTk.PhotoImage(Image.open(path1))
		self.fotoDadu2 = ImageTk.PhotoImage(Image.open(path2))
		 
		self.diceOne = tk.Label(self, image=self.fotoDadu)
		self.diceOne.grid(column=0, row=1)
		 
		self.diceTwo = tk.Label(self, image=self.fotoDadu2)
		self.diceTwo.grid(column=1, row=1)
# Nadya --------------------------------------------------------------------------

# Javier -------------------------------------------------------------------------
class App:
	def __init__(self):
		self.settings = Settings()
		self.app = Window(self)

	def run(self):
		self.app.mainloop()

if __name__ == '__main__':
	random_dice = App()
	random_dice.run()
# Javier -------------------------------------------------------------------------