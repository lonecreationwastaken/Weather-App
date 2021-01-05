import tkinter as tk
from PIL import Image, ImageTk
from weather_data import current_temperature, weather_description, city_name


class Weather:

	sun = "sun.png"
	fog = "fog.png"
	rain = "rain.png"

	def __init__(self, title):
		self.title = title


	def label(self, text, row, column):
		information = tk.Label(text = text).grid(row = row, column = column)

	def icon(self, window, img, row, column):
		panel = tk.Label(window, image = img).grid(row = row, column = column)

	def condition(self, weather):
		weather_icon = ImageTk.PhotoImage(Image.open(weather))
		return weather_icon


	def display(self):
		window = tk.Tk()
		window.geometry("500x200")
		window.title(self.title)

		if weather_description == "fog":
			weather_icon = self.condition(self.fog)
		elif weather_description == "sun":
			weather_icon = self.condition(self.sun)
		elif weather_description == "rain":
			weather_icon = self.condition(self.rain)
		else:
			weather_icon = self.condition(self.sun)

		self.label(city_name.capitalize(), 0, 1)
		self.label(current_temperature, 1, 0)
		self.icon(window, weather_icon, 1, 2)
		window.mainloop()

main = Weather("Weather App")
main.display()
