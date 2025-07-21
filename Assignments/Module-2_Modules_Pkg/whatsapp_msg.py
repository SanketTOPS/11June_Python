"""import pywhatkit

pywhatkit.sendwhatmsg_instantly('+919724799469',"Hello Students!")"""


import pywhatkit
import time

number = "+919724799469"
message = "Hello Students!"
repeats = 10  # Change to 20 if needed

for i in range(repeats):
    try:
        pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        print(f"Sent message {i+1}")
        time.sleep(15)  # wait 15 seconds before sending the next one
    except Exception as e:
        print(f"Failed at message {i+1} due to: {e}")
        time.sleep(5)
