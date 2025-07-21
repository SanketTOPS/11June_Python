import pyautogui
import time

message = "Hello Students!"
count = 20  # Number of messages

print("You have 5 seconds to open the WhatsApp chat window...")
time.sleep(5)


for i in range(count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(0.5)  # Wait half a second between messages
