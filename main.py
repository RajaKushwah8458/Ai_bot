import pyautogui
import time

# Coordinates
app_icon = (874, 1045)
second_click = (1265, 770)
message_location = (1692, 762)

# Message to type
message = "Radhe Radhe "

# Number of repetitions
repetitions = 5

# Wait for 2 seconds to give you time to switch to the correct window
time.sleep(2)

for _ in range(repetitions):
    # Click on the app icon
    pyautogui.click(app_icon)
    time.sleep(0.5)  # Small delay to allow the action to complete
    
    # Click on the second location
    pyautogui.click(second_click)
    time.sleep(0.5)  # Small delay to allow the action to complete
    
    # Type the message
    pyautogui.write(message)
    time.sleep(0.5)  # Small delay to allow the typing to complete
    
    # Click on the third location
    pyautogui.click(message_location)
    time.sleep(0.5)  # Small delay to allow the action to complete

    # Optional delay between repetitions
    time.sleep(1)

print("Script finished executing.")