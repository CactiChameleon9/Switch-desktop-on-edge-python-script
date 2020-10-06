# ~ from pynput.mouse import Button, Controller
# ~ from pynput.keyboard import Key, Controller
import pynput, time
Button = pynput.mouse.Button
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
Key = pynput.keyboard.Key
listener = pynput.mouse.Listener

leftPressed = False
desktopCount = 4 #This needs to be changed depending on your needs
currentDesktopNumber = 1
screenWidth = 1919 #this needs to be set on your screen width resolution -1

def f_choose(num):
			if num == 1:
				keyboard.press(Key.f1)
			elif num == 2:
				keyboard.press(Key.f2)
			elif num == 3:
				keyboard.press(Key.f3)
			elif num == 4:
				keyboard.press(Key.f4)
			elif num == 5:
				keyboard.press(Key.f5)
			elif num == 6:
				keyboard.press(Key.f6)
			elif num == 7:
				keyboard.press(Key.f7)
			elif num == 8:
				keyboard.press(Key.f8)
			elif num == 9:
				keyboard.press(Key.f9)
			elif num == 10:
				keyboard.press(Key.f10)
			elif num == 11:
				keyboard.press(Key.f11)
			elif num == 12:
				keyboard.press(Key.f12)

def release_all():
			keyboard.release(Key.shift)
			keyboard.release(Key.ctrl)
			keyboard.release(Key.f1)
			keyboard.release(Key.f2)
			keyboard.release(Key.f3)
			keyboard.release(Key.f4)
			keyboard.release(Key.f5)
			keyboard.release(Key.f6)
			keyboard.release(Key.f7)
			keyboard.release(Key.f8)
			keyboard.release(Key.f9)	#I am too lazy :D
			keyboard.release(Key.f10)
			keyboard.release(Key.f11)
			keyboard.release(Key.f12)

def on_click(x, y, button, pressed):
    global leftPressed
    if button == pynput.mouse.Button.left:
        if pressed:
            leftPressed = True
        else:
            leftPressed = False


# ~ while True:
def on_move(x, y):
	#time.sleep(0.05)
	global currentDesktopNumber
	try:
		if (mouse.position[0] == 0):
			mouse.position = (screenWidth, mouse.position[1])
			
			if (currentDesktopNumber > 1):
				currentDesktopNumber=currentDesktopNumber-1
			else:
				currentDesktopNumber = desktopCount
			
			# ~ print (currentDesktopNumber)
						
			if (leftPressed):
				# ~ print ("window held")
				keyboard.press(Key.ctrl)
				keyboard.press(Key.shift)  #put the switch window desktop extra key shortcut/command
				mouse.release(Button.left) # just because... probably does not help
				f_choose(currentDesktopNumber)
				release_all()
			
			keyboard.press(Key.ctrl)
			f_choose(currentDesktopNumber)
			release_all()
			
			
		elif (mouse.position[0] == screenWidth):
			mouse.position = (1, mouse.position[1])
			
			if (currentDesktopNumber < desktopCount):
				currentDesktopNumber=currentDesktopNumber+1
			else:
				currentDesktopNumber = 1
			
			# ~ print (currentDesktopNumber)
									
			if (leftPressed):
				# ~ print ("window held")
				keyboard.press(Key.ctrl)
				keyboard.press(Key.shift)  #put the switch window desktop extra key shortcut/command
				mouse.release(Button.left) # just because... probably does not help
				f_choose(currentDesktopNumber)
				release_all()
			
			keyboard.press(Key.ctrl)
			f_choose(currentDesktopNumber)
			release_all()
			
	except Exception as e:
		print("ERROR:", e)

listener = pynput.mouse.Listener(
    on_move=on_move,
    on_click=on_click)
listener.start()
listener.join()



# ~ # Read pointer position
# ~ print('The current pointer position is {0}'.format(
    # ~ mouse.position))

# ~ # Set pointer position
# ~ mouse.position = (10, 20)
# ~ print('Now we have moved it to {0}'.format(
    # ~ mouse.position))

# ~ # Move pointer relative to current position
# ~ mouse.move(5, -5)

# ~ # Press and release
# ~ mouse.press(Button.left)
# ~ mouse.release(Button.left)

# ~ # Double click; this is different from pressing and releasing
# ~ # twice on macOS
# ~ mouse.click(Button.left, 2)

# ~ # Scroll two steps down
# ~ mouse.scroll(0, 2)
