# ~ from pynput.mouse import Button, Controller
# ~ from pynput.keyboard import Key, Controller
import pynput, time
Button = pynput.mouse.Button
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
Key = pynput.keyboard.Key
listener = pynput.mouse.Listener

leftPressed = False

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
	try:
		if (mouse.position[0] == 0):
			mouse.position = (1598, mouse.position[1])
			if (leftPressed):
				print ("window held")
				keyboard.press(Key.ctrl)
				keyboard.press(Key.alt)
				keyboard.press(Key.shift)
				mouse.release(Button.left)
				keyboard.press(Key.left)		#put the switch window desktop shortcut/command
				keyboard.release(Key.ctrl)
				keyboard.release(Key.alt)
				keyboard.release(Key.shift)
				keyboard.release(Key.left)
			else:
				keyboard.press(Key.ctrl)
				keyboard.press(Key.alt)
				keyboard.press(Key.left)		#put the switch desktop shortcut/command
				keyboard.release(Key.ctrl)
				keyboard.release(Key.alt)
				keyboard.release(Key.left)
		elif (mouse.position[0] == 1599):
			mouse.position = (1, mouse.position[1])
			if (leftPressed):
				print ("window held")
				keyboard.press(Key.ctrl)
				keyboard.press(Key.alt)
				keyboard.press(Key.shift)
				mouse.release(Button.left)
				keyboard.press(Key.right)		#put the switch window desktop shortcut/command
				keyboard.release(Key.ctrl)
				keyboard.release(Key.alt)
				keyboard.release(Key.shift)
				keyboard.release(Key.right)
			else:
				keyboard.press(Key.ctrl)
				keyboard.press(Key.alt)
				keyboard.press(Key.right)
				keyboard.release(Key.ctrl)
				keyboard.release(Key.alt)
				keyboard.release(Key.right)
	except:
		print ("an error occured")

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
