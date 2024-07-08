import pyautogui
import time
import numpy as np

def isDebug() -> bool:
    print("DEBUG will show mouse position and operations in your terminal.")
    q = str(input("Enable Debug Mode? [y/n] "))
    
    if q == "n":
        return False
    elif q == "y":
        return True
    else:
        print("InputError: please enter [y/n]...")
        print("[DEFAULT] DEBUG: ON")
        return True

    
def sleepTime() -> int:
    print("\nHow long do you want to wait between inputs?\n" + "Example: 5 = sleep for 5 seconds")
    try:
        s = int(input("Enter Sleep Time in seconds: "))
        if s > 180:
            print("\nERROR: Too long...")
            print("Defaulting to 5")
            return 5
        return s
    except ValueError:
        print("\nValueError: please enter a number less than 180...")
        print("[DEFAULT] sleeping for 5 seconds...")
        return 5
    
def run_app(debug: bool, sleepTime: int) -> None:
    print('\npress "ctrl-c" to quit...')
    size = pyautogui.size()
    
    print(size) if debug == True else ""
        
    pyautogui.FAILSAFE = False

    while True:
        try:
            time.sleep(sleepTime)
            
            x = np.random.randint(1, size[0])
            y = np.random.randint(1, size[1])
            pyautogui.moveTo(x, y)
            print("[DEBUG] POS: ", x, y) if debug == True else ""
            
            pyautogui.scroll(300, x, y)
            print("[DEBUG] SCROLL: ", "UP") if debug == True else ""
            pyautogui.scroll(-300, x, y)
            print("[DEBUG] SCROLL: ", "DOWN") if debug == True else ""
            
            pyautogui.scroll(300, x, y)
            print("[DEBUG] SCROLL: ", "UP") if debug == True else ""
            pyautogui.scroll(-300, x, y)
            print("[DEBUG] SCROLL: ", "DOWN") if debug == True else ""
            
            print("[DEBUG] SCROLL: ", "UP") if debug == True else ""
            pyautogui.scroll(-300, x, y)
            
            for i in range(0, 3):
                pyautogui.press('shift')
                print("[DEBUG] KEY INPUT: ", "SHIFT") if debug == True else ""
                            
        except:
            print('Done')
            quit()

if __name__ == "__main__": 
    run_app(debug=isDebug(), sleepTime=sleepTime())