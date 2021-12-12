import asyncio
import aioconsole
import time

async def term(env, arg):
	#ret = 0 arret total
	#ret = 1 redemarage
	#ret = 2 continue
	ret = 2
	tmp: bool

	argTab = arg.split()
	print(argTab)

	if argTab[0] == "qqq":
		env.launchLog=False
		env.launchEvent=False
		ret = 0

	elif argTab[0] == "stop":

		if argTab[1] == "event":
			env.launchEvent=False
			print("stop event!")

		elif argTab[1] == "log":
			env.launchLog=False
			print("stop log!")

		else:
			print ("valeur inconue veulier réssayer avec event ou log")

	elif argTab[0] == "start":
		if argTab[1] == "event":
			tmp = env.launchLog
			env.launchEvent=False
			env.launchLog=False

			print(env.launchEvent)
			print("arret des service")

			await asyncio.sleep(1.0)

			env.launchEvent=True
			env.launchLog=tmp
			print("Demarage de log!")
			ret = 1

		elif argTab[1] == "log":
			tmp = env.launchEvent
			env.launchEvent=False
			env.launchLog=False

			print(env.launchEvent)
			print("arret des service")

			await asyncio.sleep(1.0)

			env.launchEvent=tmp
			env.launchLog=True
			print("Demarage de log!")
			ret = 1

		else:
			print ("valeur inconue veulier réssayer avec event ou log")


	return ret

async def guiMain(env):
	isGuiFunc=True
	ret = True
	print("Environement démarer!")

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