import pyautogui
print(pyautogui.size())

#moveTo(): use this function to move the mouse in pyautogui module
pyautogui.moveTo(100, 100, duration = 5)

#moveRel() function: moves the mouse pointer relative to its previous position
pyautogui.moveRel(0, 50, duration = 5)

#position(): function to get current position of the mouse pointer
print(pyautogui.position())

#click(): function used for clicking and draggind the mouse
pyautogui.click(100, 1000)

#code inspired by clcoding.com
