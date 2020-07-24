# Switch-desktop-on-edge-python-script
A script that implements switching / slide desktop on edge from kde plasma to any other linux desktop!! (using pynput and keyboard shortcuts)

To switch desktops just move your mouse off the screen to the next one.
You can move windows by holding down on them and then moving the mouse pointer off the screen (this is because dragging (holding down on the top bar) windows does not work on mate desktop, not tested on others - but it may just work normally.).

# Configuring the script:
# slideOnEdge.py
The slideOnEdge.py script uses a dedicated desktop number counter, meanning you can go from desktop 5 to 1 (and 1 to 5) - making it seemless
For this script to work you need the following shortcuts:
- ctrl + f[desktop number here] to switch desktop
- ctrl + shift + f[desktop number here] to move active window to desktop

You also need to change the `desktopCount` variable to the number of desktops you have

# slideOnEdgeOriginal.py
The other slideOnEdgeOriginal.py script was my first attempt at this, and does not have the seemless switching like the first (going left at 1 does nothing)
For this script to work you need the following shortcuts(works with mate by default):
 - Ctrl + alt + left (switch to desktop on the left)
 - Ctrl + alt + right (switch to desktop on the right)
 - Ctrl + alt + shift left (switch to desktop on the left taking the current window with you) 
 - Ctrl + alt + shift right (switch to desktop on the right taking the current window with you)
