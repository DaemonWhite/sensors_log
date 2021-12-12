import asyncio

def term(env, arg):
	argTab = arg.split()
	print(argTab)

	if argTab[0] == "qqq":
		env.launchLog=False
		env.launchEvent=False
		return False

async def guiMain(env):
	isGuiFunc=True
	print("Environement démarer!")
	while isGuiFunc:
		arg = input("> ")
		isGuiFunc = term(env, arg)