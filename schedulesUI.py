from faulthandler import disable
from tkinter import DISABLED
from Class import *
from Generator import generator, print_escola

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Grid(GridLayout):
	def __init__(self, **kwargs):
		super(Grid, self).__init__(**kwargs)

		#Grids
		self.rows = 2 #Grid principal
		self.bottom = GridLayout(); self.bottom.cols = 2 #Grid da row inferior
		self.input = GridLayout(); self.input.rows = 4; self.input.cols = 2 #Grid da zona de input

		#Criar widgets
		self.button_generate = Button(text="Gerar Escola", font_size = 40)
		self.button_generate.bind(on_press = self.gerar_escola)

		self.label_schedules = Label(text = "SCHEDULES MOTHERFUCKER\n\n      resultados no terminal", font_size = 40)
		self.nstores = Label(text = "nº Stores:")
		self.nturmas = Label(text = "nº Turmas:")
		self.nsubjects = Label(text = "nº Disciplinas:")
		self.nsalas = Label(text = "nº Salas:")

		self.input_nstores = TextInput()
		self.input_nturmas = TextInput()
		self.input_nsubjects = TextInput()
		self.input_nsalas = TextInput()

		#Adicionar widgets
			#Top Row
		self.add_widget(self.label_schedules)

			#Bottom Row
		self.add_widget(self.bottom) #adiciona a uma nova grid bottom row da grid principal
		self.bottom.add_widget(self.button_generate)
		self.bottom.add_widget(self.input) #adiciona a grid input à direita da bottom row

			#Input
		self.input.add_widget(self.nstores)
		self.input.add_widget(self.input_nstores)
		self.input.add_widget(self.nturmas)
		self.input.add_widget(self.input_nturmas)
		self.input.add_widget(self.nsubjects)
		self.input.add_widget(self.input_nsubjects)
		self.input.add_widget(self.nsalas)
		self.input.add_widget(self.input_nsalas)

	def gerar_escola(self, instance):
		try:
			nstores = int(self.input_nstores.text)
			nturmas = int(self.input_nturmas.text)
			nsubjects = int(self.input_nsubjects.text)
			nsalas = int(self.input_nsalas.text)
			escola = generator(nsalas,nstores,nturmas,nsubjects)
			print_escola(escola)
		except:
			print("\nerror: valores não inseridos ou inválidos\n")

class scheduler(App):
	def build(self):
		return Grid()

if __name__ == "__main__":
	scheduler().run()