class ui:
	def __init__(self, term=True):
		self.term = term

	def syntaxLog(self, typeMes, message):
		if self.term:
			self.syntaxTermLog(typeMes, message)
		else:
			self.syntaxGuiLog(typeMes, message)

	def syntaxGuiLog(self, typeMes, message):
		print("hello")

	def syntaxTermLog(self, typeMes, message):
		if typeMes == 0:
			textTypeMess = "\033[94m[Info]"

		elif typeMes == 1:
			textTypeMess = "\033[93m[Avertissement]"

		elif typeMes == 2:
			textTypeMess = "\033[91m[Erreur]"

		print(textTypeMess,"\033[0m",message)