#!/usr/bin/python3
import asyncio
import aioconsole
import time

import conf as ini
import file

def syntaxTermLog(typeMes, message):

	if typeMes == 0:
		textTypeMess = "\033[94m[Info]"

	elif typeMes == 1:
		textTypeMess = "\033[93m[Avertissement]"

	elif typeMes == 2:
		textTypeMess = "\033[91m[Erreur]"

	print(textTypeMess,"\033[0m",message)

async def systemLauch(env, defEvent, defLog):
	env.launchEvent=False
	env.launchLog=False

	syntaxTermLog(0, "Arrêt des services")

	await asyncio.sleep(1.0)

	env.launchEvent=defEvent
	env.launchLog=defLog

async def term(env, arg):
	#ret = 0 arret total
	#ret = 1 redemarage
	#ret = 2 continue
	ret = 2
	tmp: bool

	argTab = arg.split()
	print(len(argTab))

	nbTabWrap = len(argTab)

	if argTab[0] == "qqq":
		env.launchLog=False
		env.launchEvent=False
		ret = 0

	elif argTab[0] == "stop":

		if nbTabWrap >= 2:
			if argTab[1] == "event":
				env.launchEvent=False
				syntaxTermLog(0, "Enregistrement... Fin des événements")

			elif argTab[1] == "log":
				env.launchLog=False
				syntaxTermLog(0, "Enregistrement... Fin des événements")

			else:
				syntaxTermLog(2, "Valeur inconnue veuillez réessayer avec event ou log")
		else:
			syntaxTermLog(1, "Il manque un paramètre")

	elif argTab[0] == "start":

		if nbTabWrap >= 2:
			if argTab[1] == "event":
			
				await systemLauch(env, True, env.launchLog)
	
				syntaxTermLog(0, "Démarrage de Event !")
				ret = 1

			elif argTab[1] == "log":

				await systemLauch(env, env.launchEvent, True)
				syntaxTermLog(0, "Démarrage de Log !")
				ret = 1

			else:
				syntaxTermLog (1, "Valeur inconnue veuillez réessayer avec event ou log")
		else:
			syntaxTermLog(1, "Il manque un paramètre")

	elif argTab[0] == "path":
		if nbTabWrap >= 2:
			st='"'

			if argTab[1][0].find(st) != -1:
				argTab[1] = argTab[1][1::]

				path =""

				for e in argTab[1::]:

					if e.find(st) != -1:
						longe = e.find(st)

						path = path + e[0:longe]

						break
					else:
						path = path + e + " "

				ok = file.verif(path)
				ini.modify("ENVIRONEMENT","path", path)
				env.path = path
				print("Chemin changé vers : "+ path)

					
			else:
				syntaxTermLog(2, "Le chemin doit être entre des guillemets")
		else:
			syntaxTermLog(1, "Il manque un paramètre")


	elif argTab[0] == "help":
		print("Sensors log ", env.version,"\nby DaemonWhite")
		print("\n\n")
		print("Démarrer les services(redémarre le programme):\nstart <log|event>\n\nArreter un service:\nstop <log|event>")
		print('\nChanger le chemin des logs\npath chemin')
		print('\nArrêt du programme\nqqq')

	else:
		syntaxTermLog(1, "Paramètre inconnu tapez help pour avoir l'aide.")


	return ret

async def guiMain(env):
	ret = False
	syntaxTermLog(0, "Environement démarré!")
	isRet =0

	while env.termEnable:
		arg = await aioconsole.ainput("> ")
		
		if not (arg):
			arg="q"

		isRet = await asyncio.gather(term(env, arg))

		if isRet[0] == 0:
			ret = False
			env.termEnable =False

		elif isRet[0] == 1:
			ret = True
			env.termEnable =False


	return ret