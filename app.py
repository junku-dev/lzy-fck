import pyautogui
import time
import numpy as np

x:int
y:int

def isDebug() -> bool:
    print("DEBUG will show mouse position and operations in your terminal.")
    q:str = input("Enable Debug Mode? [y/n]" )
    
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
        s:int = int(input("Enter Sleep time in seconds: "))
        if s > 180:
            print("\nError: Too long...")
            print("Defaulting to 5 seconds...")
            return 5
        return s
    except ValueError:
        print("\nValueError: please enter a number less than 180...")
        print("[DEFAULT] sleeping for 5 seconds...")
        return 5


def run_app(debug:bool, sleepTime:int) -> None:
    try:
        print('press "ctrl-c" to quit...')
        
        size:int = pyautogui.size()
        print(size) if debug == True else False
        try:
            while True:
                
                    time.sleep(sleepTime)
                    
                    x:int = np.random.randint(1,size[0])
                    y:int = np.random.randint(1,size[1])
                    for i in range(0, 50):
                        pyautogui.moveTo(x,y)
                        print("[DEBUG] POS:", x, y) if debug == True else ""
                        if i == 0 and x > size[0] or y > size[0]:
                            x = np.random.randint(1,size[0])
                            y = np.random.randint(1,size[1])
                            continue
                        x += 2
                        y += 2
                    
                    pyautogui.scroll(300,x,y)
                    print("[DEBUG] SCROLL: UP") if debug == True else ""
                    pyautogui.scroll(-300,x,y)
                    print("[DEBUG] SCROLL: DOWN") if debug == True else ""
                    
                    pyautogui.scroll(300,x,y)
                    print("[DEBUG] SCROLL: UP") if debug == True else ""
                    pyautogui.scroll(-300,x,y)
                    print("[DEBUG] SCROLL: DOWN") if debug == True else ""
                    
                    pyautogui.scroll(300,x,y)
                    print("[DEBUG] SCROLL: UP") if debug == True else ""

                    for i in range(0,3):
                        pyautogui.press('shift')
                        print("[DEBUG] KeyPress: SHIFT") if debug == True else ""
        except Exception as e:
            print("ERROR: ", e)
            
    except KeyboardInterrupt:
        print("Done.")
        quit()  

if __name__ == "__main__":
    run_app(debug=isDebug(), sleepTime=sleepTime())
