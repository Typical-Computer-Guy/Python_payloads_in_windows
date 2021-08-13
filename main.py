# pip install pyautogui
import pyautogui
payload_str="Start-Process chrome youtube.com"
# press windows r
pyautogui.keyDown('win')
pyautogui.keyDown('r')
pyautogui.keyUp('win')
pyautogui.keyUp('r')
# write powershell and press enter
pyautogui.typewrite('powershell')
pyautogui.hotkey('enter')
# wait for powershell window to open
pyautogui.sleep(1.0)
# write the powershell payload and hit enter
pyautogui.typewrite(payload_str)
pyautogui.hotkey('enter')