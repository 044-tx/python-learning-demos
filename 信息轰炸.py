import pyautogui
import pyperclip

pyautogui.moveTo(x=940, y=1500,duration=2)
pyautogui.click()

for i in range(5):
    pyperclip.copy('bomb')
    pyautogui.hotkey('ctrl', 'v.信息轰炸')
    pyautogui.press('enter')

