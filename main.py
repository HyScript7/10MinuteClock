import time
from os import system as RunCMD
from platform import system as OsInfo

if OsInfo() == "Windows":
	RunCMD("color 03")
	RunCMD("mode con cols=40 lines=12")
	RunCMD("title Scriptian77's Clock")

while 1:
	tm = time.ctime()
	print("    ___                             ___")
	print("   / _/                            /  /")
	print(f"  / /   {tm}   / / ")
	print(" / /                             _/ /  ")
	print("/__/                            /__/   ")
	time.sleep(1)
	if OsInfo() == "Windows":
		RunCMD("cls")
	elif OsInfo() == "Linux":
		RunCMD("clear")
	else:
		for i in range(100):
			print()