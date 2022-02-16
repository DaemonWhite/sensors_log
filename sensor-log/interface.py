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
		textTypeMess = "\033[93m[Avertisement]"

	elif typeMes == 2:
		textTypeMess = "\033[91m[Erreur]"

	print(textTypeMess,"\033[0m",message)

async def systemLauch(env, defEvent, defLog):
	env.launchEvent=False
	env.launchLog=False

	syntaxTermLog(0, "Arret des services")

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
				syntaxTermLog(0, "Enregistrement des évenement arréter")

			elif argTab[1] == "log":
				env.launchLog=False
				syntaxTermLog(0, "Enregistrement des log arréter")

			else:
				syntaxTermLog(2, "valeur inconue veulier réssayer avec event ou log")
		else:
			syntaxTermLog(1, "Il manque un parametre")

	elif argTab[0] == "start":

		if nbTabWrap >= 2:
			if argTab[1] == "event":
			
				await systemLauch(env, True, env.launchLog)
	
				syntaxTermLog(0, "Demarage de Event!")
				ret = 1

			elif argTab[1] == "log":

				await systemLauch(env, env.launchEvent, True)
				syntaxTermLog(0, "Demarage de Log!")
				ret = 1

			else:
				syntaxTermLog (1, "valeur inconue veulier réssayer avec event ou log")
		else:
			syntaxTermLog(1, "Il manque un parametre")

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
				print("Chemin changer vers : "+ path)

					
			else:
				syntaxTermLog(2, "Le chemin doit etres entre des guillemet ")
		else:
			syntaxTermLog(1, "Il manque un parametre")


	elif argTab[0] == "help":
		print("Sensors log ", env.version,"\nby DaemonWhite")
		print("\n\n")
		print("Demarer les un service(redemare le programe)\nstart log|event\n\narreter un service\nstop log|event")
		print('\nChanger le chemin des log\npath chemin')

	else:
		syntaxTermLog(1, "Parametre inconue taper help pour voire l'aide")


	return ret

async def guiMain(env):
	isGuiFunc=True
	ret = True
	syntaxTermLog(0, "Environement démarer!")

	while isGuiFunc:
		arg = await aioconsole.ainput("> ")
		isRet = await asyncio.gather(term(env, arg))

		if isRet[0] == 0:
			isRet = False
			isGuiFunc =False

		elif isRet[0] == 1:
			isRet = True
			isGuiFunc =False


	return isRet